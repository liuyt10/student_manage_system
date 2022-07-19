# -*- coding:utf-8 -*-
class Course:
    '''定义课程类，包含名称，价格，周期'''
    def __init__(self,name,price,time):
        self.course_name = name
        self.course_price = price
        self.course_time = time