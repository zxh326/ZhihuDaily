# !/usr/bin/env/python
'''
暂时支持linux
windows 暂不支持
'''

import sys
from crontab import CronTab,time

def addCron():
    my_user_cron  = CronTab(user=True)

    command = 'python3' + ' ' + sys.path[0] + '/getTodayDaily.py > /var/log/zhihudaily.log'

    job = my_user_cron.new(command=command)

    job.setall(time(8,10))

    my_user_cron.write()


if __name__ == '__main__':
    addCron()