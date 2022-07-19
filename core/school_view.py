# -*- coding:utf-8 -*-
import os, sys, logging, shelve
from conf import setting
from conf import setting
from lib.class_school import School


class School_view:
    school_operate = {'1': 'add_course', '2': 'add_classroom', '3': 'add_teacher', '4': 'show_classroom',
                      '5': 'show_course', '6': 'show_teacher', '7': 'add_teacher', '8': 'exit'}

    def __init__(self):
        if os.path.exists(setting.school_file + '.dat'):
            self.school_file = shelve.open(setting.school_file)
            self.school_manager()
            self.school_file.close()


        else:
            pass

    def init_school(self):  # 创建两个学校
        self.school_file = shelve.open(setting.school_file)
        self.school_file['北京'] = School('总校', '北京')
        self.school_file['上海'] = School('总校', '上海')

    def school_manager(self):
        while True:
            for school_name in self.school_file:
                print(f'学校的名称:{school_name}')
            school_option = input('请输入要管理的学校名称>>>:').strip()
            if school_option in self.school_file:
                self.school_option = school_option
                self.school_obj = self.school_file[school_option]
            while True:
                menu = f'''
                欢迎来到  Python{school_option}校区
                1.添加课程 
                2.添加班级
                3.添加讲师
                4.查看班级
                5.查看课程
                6.查看讲师
                7.修改讲师
                8.退出
                '''
                print(menu)
                user_choice = input('请选择以上操作，输入操作对应的数字>>>:'.strip())
                if user_choice in School_view.school_operate:
                    getattr(self, School_view.school_operate[user_choice])()
                else:
                    print('操作对应的数字输入错误，请重新输入！！！！')
                    pass

    def add_course(self):
        course_name = input('请输入需要添加的课程名称>>>').strip()
        course_price = input('请输入所添加课程的价格>>>').strip()
        course_time = input('请输入课程周期>>>').strip()
        if course_name in self.school_obj.school_course:
            print('课程已经存在')
        else:
            self.school_obj.creat_course(course_name,course_price,course_time)
            print(f'%{course_name}课程添加成功')
        self.school_file.update({self.school_option:self.school_obj})
        self.school_file.close()


School_view().school_manager()
