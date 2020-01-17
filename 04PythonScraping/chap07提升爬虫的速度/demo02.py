#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import threading
import time


class myThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.delay)
        print("Exiting " + self.name)


def print_time(threadName, delay):
    counter = 0
    while counter < 3:
        time.sleep(delay)
        print(threadName, time.ctime())
        counter += 1


threads = []

# 创建新线程
thread1 = myThread("Thread-1", 1)
thread2 = myThread("Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()

print("Exiting Main Thread")