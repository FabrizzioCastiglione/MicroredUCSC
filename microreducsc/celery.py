from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microreducsc.settings')

app = Celery('microreducsc')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.timezone = 'UTC'
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-60-seconds-modbus': {
        'task': 'graph.modbus.modbustcp',
        'schedule': 60.0,
        'args': (1,502)
    }
}