
from pythonFlask.elastic.elasticUtils import ElasticUtils

if __name__=='__main__':

    index_name = 'ott'
    index_type = 'ott_type'
    _mappings = {
        "mappings": {
            index_type: {
                "properties": {
                    "title": {
                        "type": "text",
                        "index": True,
                        "analyzer": "ik_max_word",
                        "search_analyzer": "ik_max_word"
                    },
                    "date": {
                        "type": "text",
                        "index": True
                    },
                    "keyword": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "source": {
                        "type": "string",
                        "index": "not_analyzed"
                    },
                    "link": {
                        "type": "string",
                        "index": "not_analyzed"
                    }
                }
            }
        }
    }

    list = [
        {"date": "2017-09-13",
         "source": "慧聪网",
         "link": "http://info.broadcast.hc360.com/2017/09/130859749974.shtml",
         "keyword": "电视",
         "title": "付费 电视 行业面临的转型和挑战"
         },
        {"date": "2017-09-13",
         "source": "中国文明网",
         "link": "http://www.wenming.cn/xj_pd/yw/201709/t20170913_4421323.shtml",
         "keyword": "电视",
         "title": "电视 专题片《巡视利剑》广获好评：铁腕反腐凝聚党心民心"
         }
    ]

    doc = {
        "query": {
            "match": {
                "keyword": "电视"
            }
        }
    }

    obj = ElasticUtils().connectElastic("localhost", "elastic", "changeme")

    # obj.initIndex(index_name, index_type)

    obj.createIndex(_mappings)

    # obj.pushData(list)

    obj.getDataByBody(doc)

    #obj.deleteDataById("5MmxZmoBLCIquYJQTvvo")