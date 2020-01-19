#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
import _thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(threadName, time.ctime())

_thread.start_new_thread(print_time, ("Thread-1", 2))
_thread.start_new_thread(print_time, ("Thread-2", 3))
print("Main Finished")
'''

'''在使用python多线程_thread的时候，发现主线程未等待多线程进程运行完成就结束，导致多线程无效'''

import _thread
import time
from threading import Lock


def test(i):
    global unfinished_thread
    print('开始运行第%s个进程' % i)
    time.sleep(i)
    lock.acquire()
    unfinished_thread -= 1
    print('结束运行第%s个进程' % i)
    lock.release()


# 测试入口
if __name__ == '__main__':
    unfinished_thread = 0
    # 创建线程锁，用于判断线程是否全部完成
    lock = Lock()
    start_time = time.time()
    for i in range(1, 4, 1):
        try:
            # 多线程多分类同时运行
            unfinished_thread += 1
            _thread.start_new_thread(test, (i,))
        except:
            print("Error: unable to start thread" + str(i))
    while True:
        # 等待所有线程完成
        lock.acquire()
        if unfinished_thread != 0:
            lock.release()
            time.sleep(1)
            print('多线程未结束，休眠1s，剩余线程数量：%s' % unfinished_thread)
        else:
            lock.release()
            break
    print('运行完毕,耗时%s秒' % (time.time() - start_time))
