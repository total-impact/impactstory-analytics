import time
import requests
import iso8601
import logging
import redis
import os

from impactstoryanalytics.widgets.widget import Widget, by_hour
from impactstoryanalytics.widgets.widget_api_helpers import Keenio


logger = logging.getLogger("impactstoryanalytics.widgets.celery")

celery_redis_database_number = 1
my_celery_redis = redis.from_url(os.getenv("REDIS_URL"), celery_redis_database_number)

class Celery(Widget):

    def get_data(self):
        response = []
        for queue_name in ["core_main", "celery"]:
            response.append({"queue_name":queue_name, "queue_length":my_celery_redis.llen(queue_name)})
        logger.info(u"celery queue length: {response}".format(
            response=response))
        return response



       