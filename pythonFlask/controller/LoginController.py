from flask import *     #导入蓝图
custLogin=Blueprint('custLogin',__name__) #在本模块实例化1个蓝图

@custLogin.route('/',methods=['GET'])
def login():
    return render_template('/login.html')

@custLogin.route('/doLogin',methods=['POST'])
def doLogin():
    username = request.form.get('username')
    password = request.form.get('password')

    print('username: %s ' % username)
    print('password: %s ' % password)

    info = dict()
    info['statusCode'] = 200
    return jsonify(info)


@custLogin.route('/loginSuccess',methods=['GET'])
def loginSuccess():
    return render_template('/index.html')