# !/usr/bin/env/python
'''
暂时支持linux
windows 暂不支持
'''

import sys
from crontab import CronTab, time
from getConfig import UpdateFirstRunStatus


def addCron():
    my_user_cron = CronTab(user=True)

    command = 'python3' + ' ' + sys.path[0] + \
        'getTodayDaily.py > /var/log/zhihudaily.log'
    command1 = 'python3' + ' ' + \
        sys.path[0] + 'cronset.py > /var/log/zhihudaily.log'
    job = my_user_cron.new(command=command)
    job1 = my_user_cron.new(command=command1)

    job.setall(time(8, 10))
    job1.setall(time(0, 0))

    my_user_cron.write()
    UpdateFirstRunStatus('False')
if __name__ == '__main__':
    addCron()
