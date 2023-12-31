import logging
from logstash_async.handler import AsynchronousLogstashHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logstash_handler = AsynchronousLogstashHandler(
    host='localhost', port=5929,
    database_path='',
    flush_period=5
)
logger.addHandler(logstash_handler)

text_file_path = 'D:/Server/nginx-1.24.0/logs/ac.txt'
with open(text_file_path, 'r') as text_file:
    for line in text_file:
        logger.info(line.strip())
