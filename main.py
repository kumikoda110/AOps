#!/usr/bin/python
#-*- coding: utf-8 -*-


# coding:utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask, render_template, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '2EsDrsG3qeLWsrXHtLmRRj4P'

from modules import user, conf,message


@app.route('/')
def index():
    return redirect(url_for('view_monitor'))


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


@app.route('/user/reg', methods=['POST', 'GET'])
def reg():
    result = {}
    if request.method == 'POST':  # 注册按钮
        reg_info = request.form.to_dict()
        u = user.User(reg_info=reg_info)
        result = u.reg()
        if result.get('code', 54) == 0:
            return redirect(url_for('index'))
    return render_template('reg.html', result=result)


@app.route('/user/info', methods=['POST', 'GET'])
def user_info():
    u = user.User()
    if request.method == 'POST':
        phone = request.form['phone']
        result = u.status_on(phone=phone)
        return redirect(url_for('user_info'))

    result = u.user_info()
    return render_template('user_info.html', result=result)


@app.route('/user/edit', methods=['POST', 'GET'])
def user_edit():
    result = {}
    code = message = None

    u = user.User()
    if request.method == 'POST':
        phone = request.form['phone']
        username = request.form['username']
        class_type = request.form['class_type']
        class_num = request.form['class_num']
        sex = request.form['sex']
        qq = request.form['qq']
        edit_result = u.edit_user(phone=phone,
                                  username=username,
                                  class_type=class_type,
                                  class_num=class_num,
                                  sex=sex,
                                  qq=qq)
        code, message = edit_result['code'], edit_result['message']

    phone = session['phone']
    result = u.fetch_user(phone=phone)
    return render_template('user_edit.html', result=result, code=code, message=message)

@app.route('/message/usage')
def message_usage():
    result = {}
    return render_template('message_usage.html',result=result)

@app.route('/message/log')
def message_log():
    m = message.Message()
    result = m.log()
    return render_template('message_log.html',result=result)

@app.route('/message/send', methods=['POST','GET'])
def message_send():
    result = {}
    if request.method == 'POST':
        mes_info = request.form.to_dict()
        m = message.Message()
        result = m.send(**mes_info)
    return render_template('message_send.html',result=result)

@app.route('/message/notify',methods=['POST','GET'])
def message_notify():
    result = {}
    if request.method == 'POST':
        mes_info = request.form.to_dict()
        m = message.Message()
        result = m.notify(**mes_info)
    return render_template('message_notify.html',result=result)

@app.route('/api/monitor')
def api_monitor():
    m = monitor.Monitor()
    result = m.get_all_info()
    return jsonify(result)

@app.route('/monitor')
def view_monitor():
    return render_template('monitor.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)
