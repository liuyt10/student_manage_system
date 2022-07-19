# -*- coding:utf-8 -*-
import time, os, sys, shelve
from lib.class_teacher import Teacher
from lib.class_course import Course
from lib.class_classroom import Class_room
from lib.class_student import Student


class School:
    '''学校类，包含名称，地址，课程，班级，教师，学生'''

    def __init__(self, name, addr):
        self.school_name = name
        self.school_addr = addr
        self.school_course = {}  # 学校所有的课程实例，{'课程名':'课程实例'}
        self.sch_class_room = {}  # 学校所有的班级实例，{'班级名':'班级实例'}
        self.sch_teacher = {}  # 学校所有的老师实例，{'老师名':'老师实例'}
        self.sch_student = {}  # 学校所有的学生实例，{'学生名':'学生实例'}

    '''创建课程'''

    def create_course(self, course_name, course_price, course_time):
        course_obj = Course(course_name, course_price, course_time)  # 创建课程对象
        self.school_course[course_name] = course_obj  # 根据课程名为key，课程对象为value创建对应关系传进了init self.school_course

    '''展示课程'''

    def show_course(self):
        for course in self.school_course:
            course_obj = self.school_course[course]
            print(course_obj.__dict__)
            print(
                f'所在分校:{self.school_name} \t 课程名称:{course_obj.course_name} \t 课程价格:{course_obj.course_price} \t 课程周期:{course_obj.course_time}')

    '''修改课程'''

    def modify_course(self):  # 可能会继续追加、保留
        for course in self.school_course:
            course_obj = self.school_course[course]
            course_obj.course_name = input('修改课程名称为>>>')
            course_obj.course_price = input('修改课程价格为>>>')
            course_obj.course_time = input('修改课程周期为>>>')
            print(f'该课程的名称变更为:{course_obj.course_name},价格变更为:{course_obj.course_price},周期变更为:{course_obj.course_time}')

    '''创建班级'''

    def create_classroom(self, class_name, course_obj):  # 创建classroom、关联课程
        class_obj = Class_room(class_name, course_obj)  # 创建班级对象
        self.sch_class_room[class_name] = class_obj  # 根据班级名为key，课程对象为value创建对应关系传进了init self.school_course

    '''展示班级'''

    def show_classroom(self):
        for classroom in self.sch_class_room:
            class_obj = self.sch_class_room[classroom]
            # 应该是班级名称、对应课程、对应老师、对应的student、保留
            print(f'班级名称:{class_obj.class_name},课程:{class_obj.course_obj}')
            print(class_obj.__dict__)

    '''修改班级'''

    def modify_classroom(self, classroom):
        if classroom in self.sch_class_room:
            class_obj = self.sch_class_room[classroom]
            x = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 按照根据时间修改班级省去输入
            class_obj.course_obj = input('请输入课程名称>>>:')
            y = time.strftime('%Y%m%d%H%M%S', time.localtime())
            class_obj.class_name = (y + '_' + class_obj.course_obj)
        else:
            print('该班级不存在')

    '''创建教师'''

    def create_teacher(self, teacher_name, teacher_gender, teacher_age, teacher_salary, class_name, class_obj):
        teacher_obj = Teacher(teacher_name, teacher_gender, teacher_age, teacher_salary)
        teacher_obj.add_tech_classroom(class_name, class_obj)  # 讲师关联班级
        self.sch_teacher[teacher_name] = teacher_obj

    '''查看教师'''

    def show_teacher(self):
        for teacher_name in self.sch_teacher:
            teacher_obj = self.sch_teacher[teacher_name]
            print(
                f'老师姓名:{teacher_name},老师性别:{teacher_obj.teacher_gender},老师年龄:{teacher_obj.teacher_age},老师薪资:{teacher_obj.teacher_salary}')

    '''修改教师'''

    def nodify_teacher(self, teacher_name):
        if teacher_name in self.sch_teacher:
            teacher_obj = self.sch_teacher[teacher_name]
            teacher_obj.teacher_name = input('请输入老师的新姓名>>>:')
            teacher_obj.teacher_gender = input('请输入修改的老师的性别>>>:')
            teacher_obj.teacher_age = input('请输入修改的老师的年龄>>>:')
            teacher_obj.teacher_salary = input('请输入修改的老师的薪资>>>:')
            print(
                f'该老师的姓名变更为:{teacher_obj.teacher_name},性别变更为:{teacher_obj.teacher_gender},年龄变更为:{teacher_obj.teacher_age},薪资变更为:{teacher_obj.teacher_salary}')
        else:
            print('不存在该老师')

    '''创建学生'''

    def creat_student(self, student_name, student_gender, student_age, student_score, class_name):
        student_obj = Student(student_name, student_gender, student_age, student_score)
        self.sch_student[student_name] = student_obj
        student_obj.student_classroom[class_name] = self.sch_class_room[class_name]
        # 建立学生和班级的关联关系
        class_obj = self.sch_class_room[class_name]
        class_obj.class_student[student_name] = student_obj
        # 更新班级信息
        self.sch_class_room[class_name] = class_obj

    '''查看学生'''

    def show_student(self, student_name):
        if student_name in self.sch_student:
            student_obj = self.sch_student[student_name]
            print(
                f'学生姓名：{student_name}，学生性别:{student_obj.student_gender},学生年龄:{student_obj.student_age},学生成绩:{student_obj.student_score},学生所在的班级')

    '''修改学生'''

    def modify_student(self, student_name):
        if student_name in self.sch_student:
            student_obj = self.sch_student[student_name]
            student_obj.student_name = input('请输入需要学生的新姓名>>>:')
            student_obj.student_gender = input('请输入需要学生的性别>>>:')
            student_obj.student_age = input('请输入需要学生的年龄>>>:')
            student_obj.student_score = input('请输入需要学生的成绩>>>:')
            print(
                f'该学生姓名已经变更为{student_obj.student_name},学生性别变更为:{student_obj.student_gender},学生年龄变更为:{student_obj.student_age},学生成绩变更为{student_obj.student_score}')
        else:
            print('不存在该学生')
