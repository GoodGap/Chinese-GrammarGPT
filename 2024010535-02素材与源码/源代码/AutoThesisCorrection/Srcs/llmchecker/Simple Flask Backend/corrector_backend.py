from flask import Flask, request
from flask_cors import CORS

from loguru import logger

def diff(a, b):
    """
    比较两个字符串的差异，输出需要变换的操作序列
    :param a: 字符串a
    :param b: 字符串b
    """
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
    # 记录操作序列
    res = []
    """
    Operation:
    0, not change
    1. add
    2. delete
    3. modify
    """
    i, j = m, n
    while i != 0 or j != 0:
        if i > 0 and j > 0 and a[i - 1] == b[j - 1]:
            res.append([0, ""])
            i -= 1
            j -= 1
        else:
            if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
                res.append([2, a[i - 1]])
                i -= 1
            elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
                res.append([1, b[j - 1]])
                j -= 1
            else:
                res.append([3, b[j - 1]])
                i -= 1
                j -= 1
    res.reverse()
    return res

# 功能测试
FUNC_TEST = False

if not FUNC_TEST:
    from Models.predict import *
    from Models.correction import ErrorCorrect

    ec = ErrorCorrect()
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
    content_corrected = corrector.correct(error_sentence)
    with open(r"Simple Flask Backend\Models\test.txt", "w", encoding="utf-8") as f:
        f.write(content_corrected)
    predict()
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
    # 让app在本地运行，定义了host和port
    logger.debug("正在启动Flask后端...")
    app.run(host="127.0.0.1", port=8081)
    logger.debug("后端已关闭！")
