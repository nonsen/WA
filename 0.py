'''
Написать аналоги функций min и max
'''

import random

mylist = [i for i in range(11, 45)]


def max_num(_mylist):
    _mylist.sort(reverse=True)
    print(_mylist[0])


def min_num(_mylist):
    _mylist.sort()
    print(_mylist[0])
