from elasticsearch_dsl import Search
from datetime import datetime, timedelta

from elasticsearch import Elasticsearch
es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])

filter_criteria = {"query": {"match": {"message": "Hello I am Ekaghni"}}}

s = Search(using=es, index="logstash*")
s = s.update_from_dict(filter_criteria)
response = s.execute()

print(response)
for hit in response:
    print(f"Timestamp: {hit['@timestamp']},  Message: {hit.message}")
