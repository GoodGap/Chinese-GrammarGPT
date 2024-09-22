from flask import Flask, request
from flask_cors import CORS
import pycorrector
import sys
import json
from loguru import logger

sys.path.append("..")
# 初始化 flask app
app = Flask(__name__)
# app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
CORS(app, resources=r'/*', supports_credentials=True)


# 纠错接口
@app.route('/correct/', methods=['GET', 'POST'])
def correct():
    data = request.get_data()
    logger.debug("收到前端请求数据")
    logger.debug("正在解析请求数据...")
    # print(data)
    string = str(data, 'utf-8')
    # print(string)
    error_sentence = string.split('text=', 1)[1]
    # print(error_sentence)
    logger.info("提取出待纠错句子为：{}", error_sentence)
    # print(error_sentence)
    logger.debug("正在分析并纠错...")
    corrected_sent, detail = pycorrector.correct(error_sentence)
    # print(corrected_sent, detail)
    logger.info("改正后句子为：{}", corrected_sent)
    logger.info("纠错信息为：{}", detail)
    response = {'matches': []}
    for i in detail:
        match = {'message': "'" + i[0] + "'拼写错误", 'offset': i[2], 'length': i[3] - i[2],
                 'replacements': [{'value': i[1]}], 'rule': {'issueType': 'misspelling'}}
        response['matches'].append(match)
    # print(response)
    logger.debug("成功生成返回信息！")
    logger.info("返回信息为：{}", response)
    return response


# 返回本地访问地址

if __name__ == "__main__":
    # 让app在本地运行，定义了host和port
    logger.debug("正在启动Flask后端...")
    app.run(host='0.0.0.0', port=8081)
    logger.debug("后端已关闭！")
