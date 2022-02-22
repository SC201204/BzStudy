# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BzStudy
# FileName:     join线程
# Author:       SGQ
# Datetime:    2022-02-21 16:35
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
    # 主线程等待子线程
    t1.join()
    t2.join()
    print("主线程end")