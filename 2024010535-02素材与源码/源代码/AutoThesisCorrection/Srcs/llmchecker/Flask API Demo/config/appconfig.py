import os
import sys

# 项目根路径
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
# 数据存放路径
DATA_PATH = os.path.join(BASE_PATH, "data")
os.makedirs(DATA_PATH, exist_ok=True)
# 临时文件存放路径
TEMP_PATH = os.path.join(BASE_PATH, "temp")
os.makedirs(TEMP_PATH, exist_ok=True)


def config_app(app):
    app.config["JSON_AS_ASCII"] = False  # jsonify返回的中文正常显示
    app.config["UPLOAD_FOLDER"] = os.path.join(BASE_PATH, "data")
