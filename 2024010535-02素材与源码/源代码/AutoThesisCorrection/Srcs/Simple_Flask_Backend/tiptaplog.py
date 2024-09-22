# coding=UTF-8
from flask import Flask, request
from flask_cors import CORS

from loguru import logger

# 功能测试
FUNC_TEST = False
if not FUNC_TEST:
    # from Models.predict import *
    # from Models.differ import diff
    # from Models.correction import ErrorCorrect

    # ec = ErrorCorrect()
    from corrector.gecllm import LLMCorrector

    corrector = LLMCorrector()
# sys.path.append("..")
# from MuCGEC.models.seq2seq_based_CGEC.predict import *
# from MuCGEC.models.seq2seq_based_CGEC.differ import diff
# from MuCGEC.models.seq2seq_based_CGEC.correction import ErrorCorrect
# from MuCGEC import *


# 初始化 flask app
app = Flask(__name__)
# app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
CORS(app, resources=r"/*", supports_credentials=True)

def getMatched(old_content, new_content):
    differs = diff(old_content, new_content)
    print(differs)
    response = {"matches": []}  # 列表
    error_begin = 0
    error_index = 0
    last_type = 0
    issue_types = ["insert", "delete", "replace"]  # 枚举错误类型
    replacement = ""
    for i, e in enumerate(differs):
        if e[0] != last_type:
            if last_type != 0:  # 需要添加上一个错误
                if last_type == 2:
                    replacement = ""
                error_word = "".join(old_content[error_begin:error_index])

                if not (error_word.strip() == "" and last_type == 2):  # 去除删除空格的错误
                    error_message = "'" + error_word + "'错误"
                    match = {
                        "message": "残缺" if last_type == 1 else error_message,
                        "offset": error_begin,
                        "length": error_index - error_begin,
                        "replacements": [{"value": replacement}],
                        "rule": {"issueType": issue_types[last_type - 1]},
                    }
                    response["matches"].append(match)
                replacement = ""
            # 重新开始一个错误的记录
            last_type = e[0]
            error_begin = error_index
        replacement += e[1]
        if e[0] != 1:
            error_index += 1
    if last_type != 0:  # 需要添加上一个错误
        if last_type == 2:
            replacement = ""
        error_word = "".join(old_content[error_begin:error_index])

        if not (
            error_word.strip() == "" and last_type == 2 and last_type == 1
        ):  # 去除删除空格的错误
            error_message = "'" + error_word + "'错误"
            match = {
                "message": "残缺" if last_type == 1 else error_message,
                "offset": error_begin,
                "length": error_index - error_begin,
                "replacements": [{"value": replacement}],
                "rule": {"issueType": issue_types[last_type - 1]},
            }
            response["matches"].append(match)
    return response


# 纠错接口
@app.route("/correct/", methods=["GET", "POST"])
def correct():
    data = request.get_data()
    logger.debug("收到前端请求数据")
    logger.debug("正在解析请求数据...")
    # print(data)
    string = str(data, "utf-8")
    # print(string)
    error_sentence = string.split("text=", 1)[1]
    # content_corrected = ec.correct(error_sentence)
    content_corrected = corrector.GEC_Correction(error_sentence)
    with open(r"Simple Flask Backend\Models\test.txt", "w", encoding="utf-8") as f:
        f.write(content_corrected)
    # predict()
    with open(r"Simple Flask Backend\Models\res.txt", "r") as f:
        content_corrected_2 = f.read()
    content_corrected_2 = content_corrected_2.replace(" ", "")

    response = getMatched(error_sentence, content_corrected_2)
    logger.debug(error_sentence)
    logger.debug(content_corrected_2)
    logger.debug(response)
    return response


# 返回本地访问地址
if __name__ == "__main__":
    if not FUNC_TEST:
        # 让app在本地运行，定义了host和port
        logger.debug("正在启动Flask后端...")
        app.run(host="127.0.0.1", port=8081)
        logger.debug("后端已关闭！")
    else:
        result = {
            "old_content": "少先队员因该为老人让座。  真麻烦你了，希望你们好好地跳无。  我们认真学习是为了取得更优异的分数。  作者对希腊哲学史进行意义上的精雕细刻和通史意义上的古今互释。  南昌八一起义纪念馆里陈列着好多种当年周恩来使用过的东西。  一个人思想品格的好坏，关键在于内因起决定性作用。  难道能否定这次讨论会没有取得很大 成功吗？  但是应该看到，我们国家的经济基础还比较低。  在万恶的旧社会，逼得我们穷人逃荒要饭，卖儿卖女，家破人亡。  这办法既卫生，又方便，深受群众所喜爱。  过了 一会儿，汽车突然渐渐地停下来了。",
            "new_content": "少先队员应该为老人让座。真麻烦你们了，希望你们能好好地跳舞。我们认真学习是为了取得更优异的成绩。作者对希腊哲学史进行了精雕细刻和通史意义上的古今互释。南昌八一起义纪念馆里陈列着好多当年周恩来使用过的东西。一个人思想品格的好坏，关键在\n",
            "edit_list": [
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [3, "应"],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [2, " "],
                [2, " "],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [1, "们"],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [1, "能"],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [3, "舞"],
                [0, ""],
                [2, " "],
                [2, " "],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [3, "成"],
                [3, "绩"],
                [0, ""],
                [2, " "],
                [2, " "],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [3, "了"],
                [2, "义"],
                [2, "上"],
                [2, "的"],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [2, " "],
                [2, " "],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [2, "种"],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [2, " "],
                [2, " "],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [0, ""],
                [3, "\n"],
                [2, "内"],
                [2, "因"],
                [2, "起"],
                [2, "决"],
                [2, "定"],
                [2, "性"],
                [2, "作"],
                [2, "用"],
                [2, "。"],
                [2, " "],
                [2, " "],
                [2, "难"],
                [2, "道"],
                [2, "能"],
                [2, "否"],
                [2, "定"],
                [2, "这"],
                [2, "次"],
                [2, "讨"],
                [2, "论"],
                [2, "会"],
                [2, "没"],
                [2, "有"],
                [2, "取"],
                [2, "得"],
                [2, "很"],
                [2, "大"],
                [2, "成"],
                [2, "功"],
                [2, "吗"],
                [2, "？"],
                [2, " "],
                [2, " "],
                [2, "但"],
                [2, "是"],
                [2, "应"],
                [2, "该"],
                [2, "看"],
                [2, "到"],
                [2, "，"],
                [2, "我"],
                [2, "们"],
            ],
        }
        print(getMatched(result["old_content"], result["new_content"]))
