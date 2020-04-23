
from elasticsearch import Elasticsearch
import uuid

class ElasticUtils:

    def __init__(self):
        print('init elastic......')

    def connectElastic(self, es_ip, es_user, es_psw, es_port=9200):
        self.es_ip = es_ip
        self.es_user = es_user
        self.es_psw = es_psw
        self.es_port = es_port
        self.es = Elasticsearch([self.es_ip], http_auth=(self.es_user, self.es_psw), port=es_port)
        return self

    def initIndex(self, index_name, index_type):
        self.index_name = index_name
        self.index_type = index_type
        return self

    def judgePrep(self):
        if not hasattr(self, 'index_name') or self.index_name == '':
            print('index_name cannot be empty. please call "initIndex()" function.')
            return False
        if not hasattr(self, 'index_type') or self.index_type == '':
            print('index_type cannot be empty. please call "initIndex()" function.')
            return False
        return True

    def createIndex(self, mappting, _id=''):
        if not self.judgePrep():
            return
        index_id = _id
        if index_id == '':
            index_id = uuid.uuid4()

        if self.es.indices.exists(index=self.index_name) is not True:
            res = self.es.create(index=self.index_name, doc_type=self.index_type, id=index_id, body=mappting)
            print(res)
        else:
            print('[%s] already exists.' % self.index_name)
        return self

    def pushData(self, items=[]):
        if not self.judgePrep():
            return
        if len(items):
            for item in items:
                res = self.es.index(index=self.index_name, doc_type=self.index_type, body=item)
                print(res)
        else:
            print('data cannot be empty.')

    def deleteDataById(self, _id=""):
        if not self.judgePrep():
            return
        if _id == '':
            _result = self.es.delete(index=self.index_name, doc_type=self.index_type, id=id)
            print(_result)
            return _result
        else:
            print('id cannot be empty.')

    def getDataById(self, _id=""):
        if not self.judgePrep():
            return
        if _id == '':
            _result = self.es.get(index=self.index_name, doc_type=self.index_type, id=id)
            for hit in _result['hits']['hits']:
                print(hit['_source']['date'], hit['_source']['source'], hit['_source']['link'], hit['_source']['keyword'], hit['_source']['title'])
            return _result
        else:
            print('id cannot be empty.')

    def getDataByBody(self, _body={}):
        if not self.judgePrep():
            return
        if any(_body):
            _result = self.es.search(index=self.index_name, body=_body)
            for hit in _result['hits']['hits']:
                print(hit['_source']['date'], hit['_source']['source'], hit['_source']['link'], hit['_source']['keyword'], hit['_source']['title'])
            return _result
        else:
            print('body cannot be empty.')
