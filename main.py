# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime
import time
import random
import requests
import json
# 슬랙sdk - 웹클라이언트


def daytimepick():
    now = datetime.datetime.now().day
    coffeeday = random.randint(now, now + 5)

    t1 = random.randint(12, 16)
    if t1 < 16:
        t2 = random.randint(0,60)
    else:
        t2 = random.randint(0,31)
    return '{}일 {}시 {}분 ㄱㄱ'.format(coffeeday, t1, t2)


def doornot():
    coffee = random.randint(0,1)
    return coffee


def coffeeweek():
    if datetime.datetime.now().weekday() == 3:
        if doornot():
            print(daytimepick())
        else:
            print('이번 주는 없습니다.. 고난의 주를 보내시죠..')
    else:
        print(datetime.datetime.now().weekday())


if __name__ == '__main__':
    coffeeweek()


# 슬랙
# 슬랙.chat_postMessage(channel='서울잡담방', text='{}'.format(coffeeweek()))

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
