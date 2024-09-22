import requests
import json
import os
import shutil


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
error_types = [ "成分冗余", "结构混乱", "不合逻辑"]
max_iters = 1000  # 一个语病类型进行的对话轮数
sentences_per_chat = 20  # 一次对话生成的句子数
prompt_format = f"现在假设你是一个中文语言学专家。现在，你需要生成一些具有指定类型的语病的句子。在接下来的任务中，我将输入一个语病类型。你需要生成 {sentences_per_chat} 个具有我给定的语法错误的具有学术论文风格的句子。你的输出应该是 json 格式。json 的三个键分别是有语病的句子、语病的类型和改正后的句子。请你不要输出除了 json 格式的答案之外的其它语句。\n语病类型："
output_path = os.path.join("ptuning", "ptuning_data")  # 数据集输出路径

# 建立输出目录
if os.path.exists(output_path):
    shutil.rmtree(output_path)
os.makedirs(output_path)

# 输出日志
output_log_file = open(os.path.join(output_path, "output_log.txt"), "w")
output_data = open(os.path.join(output_path, "output_data.txt"), "w")

# 获取模型网址
model_url = get_model_url()

for error_type in error_types:
    cnt = 0  # 正确数据计数器
    print(f"正在生成{error_type}数据集...")
    output_log_file.write(f"正在生成{error_type}数据集...\n")
    for i in range(max_iters):
        prompt = prompt_format + error_type + "\n"
        print(f"正在进行第{1 + i}轮对话...")
        output_log_file.write(f"正在进行第{1 + i}轮对话...\n")
        try:
            response = chat(model_url, [prompt])
            if len(response) != 1:
                print(f"第{1 + i}轮对话，LLM 未给出任何答案。")
                output_log_file.write(f"第{1 + i}轮对话，LLM 未给出任何答案。\n")
                continue
            response = response[0]
            output_log_file.write(response)
        except:
            print(f"第{1 + i}轮对话，LLM 未响应。")
            output_log_file.write(f"第{1 + i}轮对话，LLM 未响应。\n")
            continue
        try:
            parsed_responses = json.loads(
                response[response.find('['):1 + response.find(']')])
        except:
            print(f"第{1 + i}轮对话，LLM 未能给出正确格式的应答，应答详情见 log。")
            output_log_file.write(
                f"第{1 + i}轮对话，LLM 未能给出正确格式的应答。应答详情\n{response}\n")
            continue
        for response in parsed_responses:
            try:
                sentence = response["有语病的句子"]
                check_prompt = f"请问这句话有没有语病：{sentence}，你只用回答“有”或“无”，不要输出任何其它语句。"
                result = chat(model_url, [check_prompt])[0]
                if result.find("有") != -1:
                    json.dump(response, output_data, ensure_ascii=False)
                    cnt += 1
            except:
                continue
        print(
            f"第{1 + i}轮对话，LLM 给出 {len(parsed_responses)} 个数据，迄今为止已收到有{error_type}语病的{cnt}个数据。")
        output_log_file.write(
            f"第{1 + i}轮对话，LLM 给出 {len(parsed_responses)} 个数据，迄今为止已收到有{error_type}语病的{cnt}个数据。\n")
    print(f"语病为{error_type}的数据集生成结束，共收到{cnt}个有效数据。")
    output_log_file.write(f"语病为{error_type}的数据集生成结束，共收到{cnt}个有效数据。\n")

output_data.close()
output_log_file.close()
