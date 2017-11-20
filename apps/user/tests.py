from django.test import TestCase

# Create your tests here.
from datetime import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('Tick! The time is: %s' % datetime.now())

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'cron', second='*/3', hour='*')
    scheduler.start()

