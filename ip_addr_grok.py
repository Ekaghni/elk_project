from elasticsearch import Elasticsearch
import os
import logstash
import logging
logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logstash_handler = logstash.TCPLogstashHandler('localhost', 5959, version=1)

logger.addHandler(logstash_handler)
# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
log_file_path = "D:/Server/nginx-1.24.0/logs/access.txt"

# Change working directory to the directory containing the log file
os.chdir(os.path.dirname(log_file_path))


def push_log_to_elasticsearch(log_entry):
    # Define your index name
    index_name = "nnw"

    # Push log entry to Elasticsearch
    es.index(index=index_name, body=log_entry)

def retrieve_ips_from_elasticsearch():
    # Define your index name
    index_name = "nnw"

    # Define your search query (match_all in this case)
    query = {"query": {"match_all": {}}}

    # Search in Elasticsearch
    result = es.search(index=index_name, body=query)

    # Retrieve IP addresses from the result
    ips = [hit["_source"]["log"]["client_ip"] for hit in result["hits"]["hits"]]
    
    return ips

if __name__ == "__main__":
    log_file_path = "D:/Server/nginx-1.24.0/logs/ac.txt"

    # Change working directory to the directory containing the log file
    os.chdir(os.path.dirname(log_file_path))
    print("Current Working Directory:", os.getcwd())


    # with open("D:/Server/nginx-1.24.0/logs/access.txt", "r") as log_file:
    #     for log_entry in log_file:
    #         # Push each log entry to Elasticsearch
    #         push_log_to_elasticsearch(log_entry)

    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as log_file:
            # rest of your code
            for log_entry in log_file:
                # Push each log entry to Elasticsearch
                push_log_to_elasticsearch(log_entry)
    else:
        print(f"File not found: {log_file_path}")

    # Retrieve and print IP addresses from Elasticsearch
    # ips_from_es = retrieve_ips_from_elasticsearch()
    # print("IP Addresses in Elasticsearch:")
    # for ip in ips_from_es:
    #     print(ip)
