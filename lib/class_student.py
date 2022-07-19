# -*- coding:utf-8 -*-
class Student:
    '''学生类，包含姓名，性别，年龄，分数，所在班级'''
    def __init__(self,name,gender,age,score):
        self.student_name = name
        self.student_gender = gender
        self.student_age = age
        self.student_score = score
        self.student_classroom = {}  #班级字典{班级名称：课程对象}
