# -*- coding:utf-8 -*-

import os,time,shelve
import sys
from lib.class_school import School


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)   #添加环境变量
data_path = os.path.join(BASE_DIR + '\db')
school_file = os.path.join(data_path,'school')

print(os.path.abspath(__file__))
print(school_file)