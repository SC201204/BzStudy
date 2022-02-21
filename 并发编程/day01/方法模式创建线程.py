# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BzStudy
# FileName:     方法模式创建线程
# Author:       SGQ
# Datetime:    2022-02-19 16:41
# Description：
# -----------------------------------------------------------------------------------
import time
from threading import Thread


def fun(name):
    print(f"线程{name}start")
    for i in range(3):
        print(f"{name}-->{i}")
        time.sleep(2)
    print(f"线程{name}end")


if __name__ == '__main__':
    print("主线程start")
    # 创建线程
    t1 = Thread(target=fun, name="线程1", args=("t1",))
    t2 = Thread(target=fun, name="线程2", args=("t2",))
    # 启动线程
    t1.start()
    t2.start()
    print("t1线程的名字", t1.name)
    print("t2线程的名字", t2.name)
    print("主线程end")
