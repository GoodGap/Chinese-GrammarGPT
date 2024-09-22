"""
@Description :   语法错误分类 ptuing 数据集生成
@Author      :   tqychy 
@Time        :   2023/08/14 22:44:11
"""

from tqdm import tqdm
import requests
import json
import os
import shutil
import random


def get_model_url():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    api_key = "qQ1vN7YZaKwjH8M84UgW3rWa"
    secret_key = "OQVhUmkquHjWhDIBvVRTXxCu0RA1CwjA"
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + response.json().get("access_token")


def chat(model_url: str, content_list: list[str]) -> list[str]:
    """
    将问题输入模型，输出模型返回的答案
    :params: model_url 模型的网址
    :params: content_list 对话时用户的所有问题
    :returns: 对话时模型的所有答案
    """
    headers = {'Content-Type': 'application/json'}
    req_json = {"messages": []}
    ret = []
    for content in content_list:
        # 将本轮用户的问题加载到 json
        user_content_dict = {"role": "user", "content": content}
        req_json["messages"].append(user_content_dict)
        # 调用模型进行回答
        response = json.loads(requests.request(
            "POST", model_url, headers=headers, data=json.dumps(req_json)).text)
        if "result" not in response.keys():
            if "error_msg" in response.keys():
                print(response)
            return ret if len(ret) > 0 else [""]
        response = response["result"]
        ret.append(response)
        # 将本轮模型的回答加载到 json
        model_content_dict = {"role": "assistant", "content": response}
        req_json["messages"].append(model_content_dict)
    return ret


# 设置参数
FCGEC_path = os.path.join("raw_data", "FCGEC_train.json")  # 用于生成数据集的 FCGEC 的路径
correct_sentences_path = os.path.join("raw_data", "sentence_modified.csv")
output_path = os.path.join("ptuning", "ptuning_data")  # 数据集输出路径
error_types = {  # 语法错误类型对应关系
    "IWO": "语序不当",
    "IWC": "搭配不当",
    "CM": "成分残缺",
    "CR": "成分冗余",
    "SC": "结构混乱",
    "ILL": "不合逻辑"
}
max_length = 10  # 构建的数据集的大小
train_percent = 0.9  # 训练集占比
seed = 1024  # 随机数种子
random.seed(seed)

# 读取 FCGEC 数据集 -> FCGEC_data
with open(FCGEC_path, "r", encoding="utf8") as f:
    FCGEC_data = list(json.load(f).values())

# 读取正确句子数据集
with open(correct_sentences_path, "r", encoding="gb2312") as f:
    correct_sentences = f.readlines()
correct_sentences = [sentence.strip("\n") for sentence in correct_sentences]
unused_ptr = 0

# 建立输出目录
if os.path.exists(output_path):
    shutil.rmtree(output_path)
os.makedirs(output_path)

# 输出日志
output_log = open("output_log.txt", "w")

# 构建数据集
artificial_data = []
generated_data = []
for data in FCGEC_data:
    ptuning_data = {}
    ptuning_data["sentence"] = data["sentence"]
    if data["error_flag"] == 0:
        ptuning_data["result"] = "这句话没有语病"
    else:
        try:
            ptuning_data["result"] = "这句话的语病类型是" + \
                error_types[data["error_type"]]
        except:
            continue
    artificial_data.append(ptuning_data)
print(f"人工标注的种子池的大小：{len(artificial_data)}", file=output_log)

# 获取模型网址
model_url = get_model_url()

# while len(generated_data) < max_length:
for _ in tqdm(range(max_length)):
    # 在种子池中选择数据
    selected_generated_data = []
    selected_artificial_data = random.sample(artificial_data, 6)
    if len(generated_data) >= 2:
        selected_generated_data = random.sample(artificial_data, 2)
    error_kinds = random.sample(list(error_types.values()), 2)
    selected_artificial_data.extend(selected_generated_data)
    selected_data = selected_artificial_data
    # 生成 promopt
    example_head = "现在假设你是一个中文语言学专家。现在，你需要做一些中文语病生成的任务。首先，我会向你展示一些例子，这些例子将指导你后续的工作。每个例子包含两行，第一行是一个带有语病的句子，第二行是第一行句子的语病类型。例子间以一个空行分隔。"
    # task_head = "现在，我将输入一些任务，每个任务包含两行，第一行是一个语法正确、没有语病的句子，第二行是一个期望的语病类型。你需要将任务中的正确句子（在第一行）改成具有给定语法错误（在第二行）的句子。你的输出格式应和我已经给出的例子相同,即第一行是一个带有语病的句子，第二行是第一行句子的语病类型。例子间以一个空行分隔。注意，请不要输出多余的话。"
    task_head = "现在，我将输入一个语病类型。你需要生成 2 个具有我给定的语法错误的句子。你的输出格式应包含三行，第一行是一个带有语病的句子，第二行是第一行句子经改正后的正确句子，第三行是第一行句子的语病类型。例子间以一个空行分隔。注意，请不要输出多余的话。"
    prompt_examples = ""
    # task_contents = ""
    task_contents = error_kinds[0] + "\n"
    for data in selected_data:
        prompt_examples += data["sentence"] + "\n" + data["result"] + "\n" * 2
    # for i, ptr in enumerate(range(unused_ptr, unused_ptr + 2)):
    #     task_contents += correct_sentences[ptr] + \
    #         "\n" + error_kinds[i] + "\n" * 2
    unused_ptr += 2
    examples = example_head + "\n" + prompt_examples
    tasks = task_head + "\n" + task_contents
    # 调用模型
    print("*" * 20, file=output_log)
    response = chat(model_url, [examples, tasks])
    print("EXAMPLES:", file=output_log)
    print(examples, file=output_log)
    print("TASK:", file=output_log)
    print(tasks, file=output_log)
    print("RESPONSE:", file=output_log)
    try:
        print(response[0] + "\n\n", file=output_log)
        print(response[1], file=output_log)
    except:
        print("SOME MISTAKE OCCURED!", file=output_log)
output_log.close()
