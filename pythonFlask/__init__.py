# -*- coding: utf-8 -*-
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
import pymysql
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import json

#创建项目对象
app = Flask(__name__)

#mysql数据库的引擎
engine = create_engine('mysql+pymysql://root:root@localhost:3306/wpk_demo?charset=utf8', convert_unicode=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

#导入控制层的包
from .controller import LoginController
from .controller import PeopleController

#把文件中蓝图对象注册到app里
app.register_blueprint(LoginController.custLogin,url_prefix='/custLogin') #访问login蓝图必须以url_prefix开头
app.register_blueprint(PeopleController.people,url_prefix='/people')

#导入模型层的包
from .model import PeopleEntity