import logging
import logstash
import sys
import json
import time

logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logstash_handler = logstash.TCPLogstashHandler('localhost', 5959, version=1)

logger.addHandler(logstash_handler)


while True:
    log_messages = [
        {"message": "Hello I am Ekaghni", "log_level": "ERROR", "timestamp": time.time()},
        {"message": "Trial Project of ELK", "log_level": "WARNING", "timestamp": time.time()},
        {"message": "Info in application", "log_level": "INFO", "timestamp": time.time()}
    ]
    try:
        for log_message in log_messages:
            logger.info(json.dumps(log_message))
        time.sleep(3)

    except KeyboardInterrupt:
        break
