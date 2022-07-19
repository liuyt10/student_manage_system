# -*- coding:utf-8 -*-
class Teacher:
    '''讲师类，定义姓名，性别，年龄,薪水，教授班级'''
    def __init__(self,name,gender,age,salary):
        self.teacher_name = name
        self.teacher_age = age
        self.teacher_gender = gender
        self.teacher_salary = salary  #薪水
        self.teacher_classroom = {}  #班级列表

    def add_tech_classroom(self,class_name,class_obj):
        self.teacher_classroom[class_name] = class_obj