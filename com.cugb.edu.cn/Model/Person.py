#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nawei'

class Person(object):
    def __init__(self,name,age):
         self.name = name
         self.age = age
         self.weight = 'weight'

    def talk(self):
         print("person is talking....")


class Chinese(Person):
    def __init__(self,name, age, language):
        Person.__init__(self,name,age)
        self.language = language
        print(self.name,self.age,self.weight,self.language)

    def talk(self):
        print('%s is speaking chinese' % self.name)

    def walk(self):
        print('is walking...')


if __name__ == '__main__':

    c1 = Chinese('bigberg',22,'Chinese')
    c1.talk()




