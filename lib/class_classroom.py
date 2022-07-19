# -*- coding:utf-8 -*-

class Class_room:
    '''定义班级类，包含名称，课程对象，学生'''
    def __init__(self,name,obj):
        self.class_name = name
        self.course_obj = obj
        self.class_student = {}  #学生字典{学生姓名：学生实例}