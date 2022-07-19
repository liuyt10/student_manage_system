# -*- coding:utf-8 -*-
#修改sys.path,把homework这个文件写到sys.path列表中
#之后所有的模块导入，都是基于homework
#from core import main
#if __name__== '__main__:
# 修改sys.path,把homework这个路径写到sys.path列表中
# 之后所有的模块导入,都是基于homework

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)  #添加环境变量

from conf import setting
from core.mian import Admin


if __name__ == '__main__':
    Admin.run('')



