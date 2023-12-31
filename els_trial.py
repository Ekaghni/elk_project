from elasticsearch import Elasticsearch

# Specify the scheme as 'http' since you are connecting to localhost
es = Elasticsearch([{"host": "localhost", "port": 9200, "scheme": "http"}])

# Check if the connection is successful
print(es.ping())

# es.indices.create(index="ekaghni")
resp = es.indices.get_alias(index="ekaghni")
print(resp)
