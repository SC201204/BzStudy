# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BzStudy
# FileName:     线程同步1_互斥锁
# Author:       SGQ
# Datetime:    2022-02-21 17:29
# Description：
# -----------------------------------------------------------------------------------
import time
from threading import Thread, Lock


class Account():
    """定义账户类"""

    def __init__(self, name, money):
        self.name = name
        self.money = money


class Drawing(Thread):
    """模拟取钱操作"""
    lock = Lock()  #锁

    def __init__(self, mun, account):
        super(Drawing, self).__init__()
        self.num = mun
        self.account = account
        self.total = 0

    def run(self) -> None:
        Drawing.lock.acquire()
        if self.account.money < self.num:
            print(f"余额不足,余额是{self.account.money}")
            return
        time.sleep(1)
        self.account.money -= self.num
        self.total += self.num
        print(f"账户{self.account.name}的余额{self.account.money}，共取了{self.total}")
        Drawing.lock.release()


if __name__ == '__main__':
    account = Account("Bank", 120)
    draw1 = Drawing(60, account)
    draw2 = Drawing(60, account)
    draw1.start()
    draw2.start()
