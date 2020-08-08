import random
import time
from huey import crontab
from config import huey


@huey.task()
def count_beans(num):
    print("start")
    print("--counted: %s" % num)
    time.sleep(3)
    print("end")
    return "count %s" % num

@huey.periodic_task(crontab(minute='*/5'))
def every_five_mins():
    print("every 5 min")

