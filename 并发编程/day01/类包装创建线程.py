# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BzStudy
# FileName:     类包装创建线程
# Author:       SGQ
# Datetime:    2022-02-19 16:54
# Description：
# -----------------------------------------------------------------------------------
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self) -> None:
        print(f"线程{self.name},start")
        for i in range(3):
            print(f"{self.name}-->{i}")
            time.sleep(2)
        print(f"线程{self.name},end")


if __name__ == '__main__':
    print("主线程start")
    # 创建线程
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    # 启动线程
    t1.start()
    t2.start()
    print("主线程end")
