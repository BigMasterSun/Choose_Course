# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:39
from interface import admin_interface
from interface import common_interface
from lib import common

admin_info = {'name': None}


def register():
    print("欢迎来到管理员注册界面！".center(30, '*'))
    while True:
        name = input("请设置管理员账号：")
        pwd = input("请设置管理员密码：")
        re_pwd = input("请再次确认密码：")
        if pwd == re_pwd:
            flag, msg = admin_interface.register_interface(name, pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print("两次输入的密码不一致，请重新输入！")


def login():
    if admin_info['name']:
        print("您已登录，无需重复登录！")
        return
    print("欢迎来到管理员登录界面！".center(30, '*'))
    while True:
        name = input("请输入账户名：")
        pwd = input("请输入密码：")
        flag, msg = common_interface.login_interface(name, pwd, 'admin')
        if flag:
            print(msg)
            admin_info['name'] = name
            break
        else:
            print(msg)


@common.login_auth('admin')
def create_school():
    print("欢迎来到创建学校界面！".center(30, '*'))
    while True:
        school_name = input("请输入学校名字：")
        school_address = input("请输入学校地址：")
        flag, msg = admin_interface.create_school_interface(admin_info['name'], school_name, school_address)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth('admin')
def create_teacher():
    print("欢迎来到创建老师界面！".center(30, '*'))
    while True:
        teacher_name = input("请输入老师的姓名：")
        flag, msg = admin_interface.create_teacher_interface(admin_info['name'], teacher_name)
        if flag:
            print(msg)
            break


@common.login_auth('admin')
def create_course():
    print("欢迎来到创建课程界面！".center(30, '*'))
    while True:
        school_list = common_interface.check_all_file('school')
        if not school_list:
            print("还未创建学校！")
            break
        print('=' * 30)
        for index, school in enumerate(school_list):
            print("编号：%s  学校：%s" % (index, school))
        print('=' * 30)
        choice = input("请输入学校编号：")
        if not choice.isdigit():
            print("请输入数字！")
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(school_list)):
            print("请输入合法编号！")
        school_name = school_list[choice]
        course_name = input("请输入要创建的课程名：")
        flag, msg = admin_interface.create_course_interface(admin_info['name'], school_name, course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


method_map = {
    '1': register,
    '2': login,
    '3': create_school,
    '4': create_teacher,
    '5': create_course
}


def admin_view():
    print("欢迎来到管理员视图！")
    while True:
        print('=' * 30)
        print('''
            1、注册
            2、登录
            3、创建学校
            4、创建老师
            5、创建课程
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
