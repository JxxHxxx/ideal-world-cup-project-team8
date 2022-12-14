import os
from dotenv import load_dotenv
from pymongo import MongoClient

from flask import render_template, request, jsonify
from . import routes

import hashlib
import jwt

load_dotenv()
mySecretKey = os.environ.get('MySecretKey')
SECRET_KEY = os.environ.get('SECRET_KEY')
client = MongoClient(mySecretKey)
db = client.worldcup


@routes.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@routes.route('/api/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest() # 암호화??

    result = db.member.find_one({'id': id_receive, 'pw': pw_hash})

    if result is not None:
        payload = {
            'id': id_receive,
            'pw': pw_hash
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        return jsonify({'result': 'success', 'token': token})
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

