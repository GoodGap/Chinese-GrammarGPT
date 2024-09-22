import os, sys
from config.setting import SERVER_PORT
from api.user import user_blueprint
from api.document import doc_blueprint
from flask import Flask
from flask_cors import CORS
from config.appconfig import config_app, BASE_PATH
from tools import check_pandoc

sys.path.insert(0, BASE_PATH)  # 将项目根路径临时加入环境变量，程序退出后失效

if __name__ == "__main__":
    check_pandoc()
    app = Flask(__name__)
    config_app(app)
    CORS(app, resources=r"/*", supports_credentials=True)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(doc_blueprint)
    # host为主机ip地址，port指定访问端口号，debug=True设置调试模式打开
    app.run(host="0.0.0.0", port=SERVER_PORT, debug=True)
