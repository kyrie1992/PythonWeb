#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nawei'
' 雇员管理 '
from Employee import Employee

def _init_emplyeeInfo():
    emp1 = Employee('emp1',4000)
    Employee.empCount=Employee.empCount+1
    print(Employee.empCount)
    print(emp1._name)


if __name__ == '__main__':
    _init_emplyeeInfo()