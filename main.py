#!/usr/bin/python
#-*- coding: utf-8 -*-


import sys

reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '2EsDrsG3qeLWsrXHtLmRRj4P'

from modules import user, conf


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/login', methods=['POST', 'GET'])
def login():
    result = {}
    if request.method == 'POST':
        user_info = request.form.to_dict()
        if 'phone' in user_info and 'passwd' in user_info:
            if user_info['phone'] and user_info['passwd']:
                u = user.User(**user_info)
                result = u.login()
                if result['code'] == 0:  # 正确跳转首页
                    session['phone'] = user_info['phone']
                    return redirect(url_for('index'))
            else:
                result = {
                    'code': 4,
                    'message': conf._code.get(4, '请填写正确完整信息')
                }
        else:
            result = {
                'code': 4,
                'message': conf._code.get(4, '请填写正确完整信息')
            }

    return render_template('login.html', result=result)


@app.route('/user/logout')
def logout():
    del session['phone']
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

