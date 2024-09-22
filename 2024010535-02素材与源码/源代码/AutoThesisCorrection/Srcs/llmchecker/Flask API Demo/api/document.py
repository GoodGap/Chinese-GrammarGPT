import flask as fl
from flask import Blueprint, request, jsonify, Response
from config.appconfig import BASE_PATH
import os
from werkzeug.utils import secure_filename
from loguru import logger
from common.redis_operate import redis_db
from tools import convertHtmlToDocx
from config.appconfig import DATA_PATH

# 存放数据的路径

doc_blueprint = Blueprint("doc", __name__)

# http://127.0.0.1:9999/doc/content/test/test.txt


@doc_blueprint.route("/file/<string:username>/<string:filename>", methods=["GET"])
def get_content(username, filename):
    logger.info(request.headers)
    token = request.headers.get("Authorization", "").strip().split(" ")[-1]
    if not token:
        return Response("token不能为空", status=401)
    redis_token = redis_db.handle_redis_token(username)
    if not redis_token:
        return Response("token已失效或用户未登录", status=401)
    if redis_token != token:
        return Response("token不正确", status=401)
    logger.info("获取文件内容")
    logger.info(filename)
    if not os.path.exists(os.path.join(DATA_PATH, username, filename)):
        logger.info("文件不存在" + os.path.join(DATA_PATH, username, filename))
        return Response(jsonify({"msg": "文件不存在"}), status=404)

    with open(os.path.join(DATA_PATH, username, filename), "rb") as f:
        content = f.read()
    response = Response(content, content_type="application/octet-stream")
    return response


@doc_blueprint.route("/delete/<string:username>/<string:filename>", methods=["DELETE"])
def delete_file(username, filename):
    token = request.json.get("token", "").strip()
    if not token:
        return jsonify({"code": 1, "msg": "token不能为空"})
    redis_token = redis_db.handle_redis_token(username)
    if not redis_token:
        return jsonify({"code": 2, "msg": "token已失效或用户未登录"})
    if redis_token != token:
        return jsonify({"code": 3, "msg": "token不正确"})
    logger.info("删除文件")
    logger.info(filename)
    if not os.path.exists(os.path.join(DATA_PATH, username, filename)):
        return jsonify({"code": 4, "msg": "文件不存在"})
    os.remove(os.path.join(DATA_PATH, username, filename))
    return jsonify({"code": 0, "msg": "删除成功"})


@doc_blueprint.route("/update/<string:username>/<string:filename>", methods=["POST"])
def update_file(username, filename):
    token = request.json.get("token", "").strip()
    if not token:
        return jsonify({"code": 1, "msg": "token不能为空"})
    redis_token = redis_db.handle_redis_token(username)
    if not redis_token:
        return jsonify({"code": 2, "msg": "token已失效或用户未登录"})
    if redis_token != token:
        return jsonify({"code": 3, "msg": "token不正确"})
    logger.info("更新文件")
    logger.info(filename)
    if not os.path.exists(os.path.join(DATA_PATH, username, filename)):
        return jsonify({"code": 4, "msg": "文件不存在"})
    content = request.json.get("content", "").strip()
    if not content:
        return jsonify({"code": 5, "msg": "文件内容不能为空"})
    logger.info("更新文件内容" + content)
    convertHtmlToDocx(content, os.path.join(DATA_PATH, username, filename))
    return jsonify({"code": 0, "msg": "更新成功"})


@doc_blueprint.route("/upload", methods=["POST"])
def upload_file():
    token = request.form.get("token", "").strip()
    if not token:
        return jsonify({"code": 1, "msg": "token不能为空"})
    username = request.form.get("username", "").strip()

    if not username:
        return jsonify({"code": 2, "msg": "用户名不能为空"})
    redis_token = redis_db.handle_redis_token(username)
    if not redis_token:
        return jsonify({"code": 3, "msg": "token已失效或用户未登录"})
    if redis_token != token:
        return jsonify({"code": 4, "msg": "token不正确"})
    logger.info("上传文件")
    file_list = request.files.getlist("files")
    if not file_list or len(file_list) == 0:
        return jsonify({"code": 5, "msg": "文件不能为空"})
    for file in file_list:
        filename = file.filename
        if not os.path.exists(os.path.join(DATA_PATH, username)):
            os.makedirs(os.path.join(DATA_PATH, username), exist_ok=True)
        file.save(os.path.join(DATA_PATH, username, filename))
    return jsonify({"code": 0, "msg": "上传成功"})


@doc_blueprint.route("/list/<string:username>", methods=["POST"])
def list_file(username):
    logger.info("列出文件")
    token = request.json.get("token", "").strip()
    if not token:
        return jsonify({"code": 1, "msg": "token不能为空"})
    redis_token = redis_db.handle_redis_token(username)
    if not redis_token:
        logger.info("token已失效或用户未登录")
        return jsonify({"code": 2, "msg": "token已失效或用户未登录"})
    if redis_token != token:
        return jsonify({"code": 3, "msg": "token不正确"})
    logger.info("列出文件")
    logger.info(username)
    if not os.path.exists(os.path.join(DATA_PATH, username)):
        return jsonify({"code": 4, "msg": "文件不存在"})
    file_list = os.listdir(os.path.join(DATA_PATH, username))
    logger.info("找到文件列表")
    logger.info(file_list)
    return jsonify({"code": 0, "msg": "获取成功", "data": file_list})
