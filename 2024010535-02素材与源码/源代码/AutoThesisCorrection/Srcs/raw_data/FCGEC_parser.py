"""
@Description :   把 FCGEC 数据集整理成给定的格式
@Author      :   tqychy 
@Time        :   2023/10/14 13:53:21
"""
"""
给定的格式：
"id": ...:
{
   
    "sentence": 错误句子
    "error_flag": 0/1,
    "error_type": 6 种语法错误之一,
    "correct_sentence": 正确句子（是一个列表）
}

"""

# 参数

import json
import re
FCGEC_train_path = "FCGEC_train.json"
FCGEC_valid_path = "FCGEC_valid.json"
save_path = "FCGEC_parsed.json"

def error_type_paser(id: int, error_types: str) -> list[str]:
    ret = []
    error_types_dict = {  # 语法错误类型对应关系
        "*": "没有语病",
        "IWO": "语序不当",
        "IWC": "搭配不当",
        "CM": "成分残缺",
        "CR": "成分冗余",
        "SC": "结构混乱",
        "ILL": "不合逻辑",
        "AM": "表意不明"
    }
    for error_type in error_types.split(";"):
        try:
            ret.append(error_types_dict[error_type])
        except:
            raise RuntimeError(f"第 {id} 个句子错误：\n未定义的语法错误类型{error_type}。")
    return ret


def operation_parser(id: int, sentence: str, operations: list[dict]) -> list[str]:
    ret = []
    for operation in operations:
        char_list = list(sentence)
        for method, code in operation.items():
            if method == "Switch":
                tmp = []
                for ind in code:
                    tmp.append(char_list[ind])
                char_list = tmp
            elif method == "Delete":
                for ind in code:
                    if ind >= len(char_list):
                        raise RuntimeError(
                            f"第 {id} 个句子 {sentence} 错误：\n要删除的字符索引超过句子的长度")
                    char_list[ind] = "^"
            elif method == "Insert":
                code = code[0]
                labels = list(code["label"])
                for j, label in enumerate(labels):
                    char_list.insert(j + code["pos"], label)
            elif method == "Modify":
                code = code[0]
                tags = code["tag"].split("+")
                labels = list(code["label"])
                char_list_ptr = code["pos"]
                labels_ptr = 0
                for tag in tags:
                    try:
                        num = re.findall(r"\d+", tag)[0]
                        op = re.findall(r"[a-zA-Z]+", tag)[0]
                    except:
                        raise RuntimeError(f"第 {id} 个句子 {sentence} 错误：\n{tag} 未按格式标注。")
                    num = int(num)
                    if op == "MOD":
                        for _ in range(min(num, len(labels))):
                            char_list[char_list_ptr] = labels[labels_ptr]
                            char_list_ptr += 1
                            labels_ptr += 1
                    elif op == "INS":
                        char_list_ptr -= 1
                        for _ in range(num):
                            char_list.insert(char_list_ptr, labels[labels_ptr])
                            char_list_ptr += 1
                            labels_ptr += 1
                    elif op == "DEL":
                        for _ in range(num):
                            char_list[char_list_ptr] = "^"
                            char_list_ptr += 1
                    else:
                        RuntimeError(
                            f"第 {id} 个句子 {sentence} 错误：\n未定义的 tag 指令：{op}。")
            else:
                RuntimeError(f"第 {id} 个句子 {sentence} 错误：\n未定义的指令：{method}。")
                continue
        ret.append("".join(char_list).replace("^", ""))
    return ret if len(operations) > 0 else [sentence]


# 读取 FCGEC 数据集 -> FCGEC_data
FCGEC_data = []
with open(FCGEC_train_path, "r", encoding="utf8") as f:
    FCGEC_data.extend(list(json.load(f).values()))
with open(FCGEC_valid_path, "r", encoding="utf8") as f:
    FCGEC_data.extend(list(json.load(f).values()))
res = {}

# 遍历数据集处理数据
for i, data in enumerate(FCGEC_data):
    res[i] = {}
    try:
        res[i]["sentence"] = data["sentence"]
        res[i]["error_flag"] = data["error_flag"]
        res[i]["error_type"] = error_type_paser(i, data["error_type"])
        res[i]["operation"] = data["operation"]
        res[i]["correct_sentence"] = operation_parser(
            i, data["sentence"], json.loads(data["operation"]))
    except:
        print(f"第 {i} 个句子 {data['sentence']} 错误：\n未按格式标注，跳过。")
        del res[i]
        continue
    
print(f"共处理句子{len(FCGEC_data)}个，成功处理{len(res)}个")

# 保存成 json 格式
with open(save_path, "w", encoding="utf8") as f:
    json.dump(res, f, ensure_ascii=False)
