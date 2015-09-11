from __future__ import absolute_import

from celery import shared_task
from celery.utils.log import get_task_logger


@shared_task(bind=True, max_retries=3, default_retry_delay=30)
def add_numbers(self, row_id):
    logger = get_task_logger(__name__)
    logger.info(u'[{0.id}]Function all_numbers called with params [{1}] with extended info:{0}'.format(
        self.request,
        row_id
    ))
    from .models import Adder
    record = Adder.objects.get(pk=row_id)
    record.result = record.x + record.y
    record.save()
