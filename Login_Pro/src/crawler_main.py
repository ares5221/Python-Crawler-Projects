#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from login_yibu import login_yibu
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    website_url_dict = {
        'yibushequ': 'https://www.epubit.com/',
        # 'dashi': 'http://www.xiexingcun.com/search.asps',
    }
    for curr_url in website_url_dict:
        if curr_url == 'yibushequ':
            login_yibu()
        elif curr_url == '':
            pass
        print('\n \n \nlogin完成\n \n \n')
        break

def login_everyday():
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour=13, minute=32)
    scheduler.start()
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(t)


if __name__ == '__main__':
    login_everyday()
