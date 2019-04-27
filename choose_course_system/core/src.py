# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:39

from . import admin
from . import student
from . import teacher
method_map = {
    '1': admin.admin_view,
    '2': teacher.teacher_view,
    '3': student.student_view
}


def run():
    print("欢迎来到选课系统！")
    while True:
        print('=' * 30)
        print('''
        1、管理员视图
        2、老师视图
        3、学生视图
        q、退出
        ''')
        print('=' * 30)
        choice = input("请选择功能编号：")
        if choice == 'q':
            break
        if choice not in method_map:
            print("输入的编号不存在！")
            continue
        method_map[choice]()