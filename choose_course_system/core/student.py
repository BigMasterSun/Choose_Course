# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:39
from interface import student_interface
from interface import common_interface
from lib import common

student_info = {'name': None}


def register():
    print("欢迎来到学生注册界面！".center(30, '*'))
    while True:
        name = input("请输入姓名：")
        pwd = input("请输入密码：")
        re_pwd = input("请再次确认密码：")
        if pwd == re_pwd:
            flag, msg = student_interface.register_interface(name, pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("两次输入的密码不一致，请重输！")


def login():
    if student_info['name']:
        print("当前已登录，无需重复登录")
        return
    print("欢迎来到学生登录界面！".center(30, '*'))
    while True:
        name = input("请输入姓名：")
        pwd = input("请输入密码：")
        flag, msg = common_interface.login_interface(name, pwd, 'student')
        if flag:
            print(msg)
            student_info['name'] = name
            break
        else:
            print(msg)


@common.login_auth('student')
def choose_school():
    print("欢迎来到选择学校界面！".center(30, '*'))
    while True:
        school_list = student_interface.get_all_school('school')
        if not school_list:
            print("没有学校可选！")
            return
        print('=' * 30)
        for index, school in enumerate(school_list):
            print('编号：%s  学校：%s'%(index, school))
        print('=' * 30)
        choice = input("请选择学校编号：")
        if not choice.isdigit():
            print("请输入数字！")
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(school_list)):
            print("请输入合法编号！")
            continue
        school_name = school_list[choice]
        flag, msg = student_interface.choose_school_interface(student_info['name'], school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.login_auth('student')
def choose_course():
    print("欢迎来到选择课程界面！".center(30, '*'))
    while True:
        # 获取学生所选的学校
        school_name = student_interface.get_school(student_info['name'])
        if not school_name:
            print("还未选择学校！")
            return
        # 获取学校下的所有可选课程
        course_list = student_interface.get_all_course(school_name)
        if not course_list:
            print("没有可选的课程！")
            return
        print('=' * 30)
        for index, course in enumerate(course_list):
            print('编号：%s  课程：%s' % (index, course))
        print('=' * 30)
        choice = input("请选择课程编号：")
        if not choice.isdigit():
            print("请输入数字！")
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(course_list)):
            print("请输入合法编号！")
            continue
        course_name = course_list[choice]
        flag, msg = student_interface.choose_course_interface(student_info['name'], course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth('student')
def check_score():
    print("欢迎来到查看成绩界面！".center(30, '*'))
    while True:
        # 获取自己选择的课程
        course_list = student_interface.get_student_course(student_info['name'])
        if not course_list:
            print("还没有选择课程！")
            return
        print('=' * 30)
        for index, course in enumerate(course_list):
            print('编号：%s  课程：%s' % (index, course))
        print('=' * 30)
        choice = input("请选择课程编号：")
        if not choice.isdigit():
            print("请输入数字！")
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(course_list)):
            print("请输入合法编号！")
            continue
        course_name = course_list[choice]
        score = student_interface.get_score_interface(student_info['name'], course_name)
        print("课程[%s]的成绩是[%s]"%(course_name,score))
        break


method_map = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score
}


def student_view():
    print("欢迎来到学生视图！")
    while True:
        print('=' * 30)
        print('''
                1、注册
                2、登录
                3、选择学校
                4、选择课程
                5、查看成绩
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