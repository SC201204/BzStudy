# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   BzStudy
# FileName:     线程同步1
# Author:       SGQ
# Datetime:    2022-02-21 17:01
# Description：
# -----------------------------------------------------------------------------------
# 未使用线程同步和锁访问统一资源
import time
from threading import Thread


class Account():
    """定义账户类"""

    def __init__(self, name, money):
        self.name = name
        self.money = money


class Drawing(Thread):
    """模拟取钱操作"""

    def __init__(self, mun, account):
        super(Drawing, self).__init__()
        self.num = mun
        self.account = account
        self.total = 0

    def run(self) -> None:
        if self.account.money < self.num:
            return
        time.sleep(1)
        self.account.money -= self.num
        self.total += self.num
        print(f"账户{self.account.name}的余额{self.account.money}，共取了{self.total}")


if __name__ == '__main__':
    account = Account("Bank", 100)
    draw1 = Drawing(60, account)
    draw2 = Drawing(60, account)
    draw1.start()
    draw2.start()
