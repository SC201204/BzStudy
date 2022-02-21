# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BzStudy
# FileName:     线程同步2_死锁
# Author:       SGQ
# Datetime:    2022-02-21 17:40
# Description：
# -----------------------------------------------------------------------------------
import time
from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()


def fun1():
    lock1.acquire()
    print("fun1拿到lock1")
    time.sleep(3)
    lock2.acquire()
    print("fun1拿到lock2")
    lock2.release()
    print("fun1释放lock2")
    lock1.release()
    print("fun1释放lock1")


def fun2():
    lock2.acquire()
    print("fun2拿到lock2")
    lock1.acquire()
    print("fun2拿到lock1")
    lock1.release()
    print("fun2释放lock1")
    lock2.release()
    print("fun2释放lock2")


if __name__ == '__main__':
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun2)
    t1.start()
    t2.start()
