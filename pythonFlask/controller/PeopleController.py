from flask import *
from pythonFlask.model import PeopleEntity as pe

people=Blueprint('people',__name__)

@people.route('/',methods=['GET'])
def index():
    return render_template('/people/peopleIndex.html')

@people.route('/list',methods=['GET'])
def list():
    page = request.args['page']
    limit = request.args['limit']
    searchName = request.args.get('searchName')

    if not searchName:
        print('searchName is not empty')

    peo = pe.PeopleEntity();#创建对象
    result = peo.query.offset(int(page)-1).limit(limit).all()#获取列表信息
    count = peo.query.count()#计算总数
    _list = peo.to_list(result);#转换为集合

    info = dict()
    info['code'] = 0
    info['count'] = count
    info['data'] = _list

    return jsonify(info)

@people.route('/detail',methods=['GET','POST'])
def detail():
    _id = request.args.get('id')
    info = dict()
    if _id is None:
        print('id is empty')
    else:
        peo = pe.PeopleEntity();#创建对象
        result = peo.query.filter_by(id = _id).first()
        info['id'] = result.id
        info['name'] = result.name
        info['age'] = result.age
        info['opera'] = result.opera
        info['remark'] = result.remark
    return render_template('/people/peopleEdit.html', bean=info)

@people.route('/save',methods=['POST'])
def save():
    info = dict()
    return jsonify(info)

@people.route('/opera',methods=['POST'])
def opera():
    info = dict()
    return jsonify(info)