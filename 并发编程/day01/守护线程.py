# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BzStudy
# FileName:     守护线程
# Author:       SGQ
# Datetime:    2022-02-21 16:37
# Description：
# -----------------------------------------------------------------------------------
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print(f"{self.name}开始运行")
        for i in range(3):
            print(f"{self.name}遍历{i}")
            time.sleep(1)
        print(f"{self.name}结束运行")


if __name__ == '__main__':
    print("主线程开始运行")
    t1 = MyThread("线程1")
    t1.setDaemon(daemonic=True)
    t1.start()
    print("主线程结束运行")
