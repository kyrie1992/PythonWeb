#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nawei'

' 定义student实体类 '
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' %(self.name, self.score))

if __name__ == '__main__':
    bart = Student('Bart Simpson',59)
    print(bart.name)


