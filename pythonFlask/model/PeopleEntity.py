from pythonFlask import *
from sqlalchemy import *

class PeopleEntity(Base):
    __tablename__ = "people"
    id = Column(Integer,primary_key=True)
    name = Column(String(64),nullable=True)
    age = Column(Integer,nullable=True)
    opera = Column(String(2),nullable=True)
    remark = Column(String(64),nullable=True)

    @staticmethod
    def to_list(data):
        return_list = list()
        for i in data:
            var_json = {
                'id': i.id,
                'name': str(i.name),
                'age': i.age,
                'opera': str(i.opera),
                'remark': str(i.remark)
            }
            return_list.append(var_json)
        return return_list

    @staticmethod
    def init_db():
        metadata.create_all(bind=engine, tables="people")