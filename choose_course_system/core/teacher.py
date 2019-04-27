# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:39
from interface import teacher_interface
from interface import common_interface
from lib import common

teacher_info = {'name': None}


def login():
    if teacher_info['name']:
        print("您已登录，无需重复登录！")
        return
    print("老师登录界面".center(30,'-'))
    while True:
        name = input("请输入姓名：")
        pwd = input("请输入密码：")
        flag, msg = common_interface.login_interface(name, pwd, 'teacher')
        if flag:
            print(msg)
            teacher_info['name'] = name
            break
        else:
            print(msg)


@common.login_auth('teacher')
def check_course():
    print("查看教授的课程界面".center(30, '-'))
    flag, msg = teacher_interface.check_course_interface(teacher_info['name'])
    if flag:
        print(msg)
    else:
        print(msg)


@common.login_auth('teacher')
def choose_course():
    print("选择教授的课程界面".center(30, '-'))
    while True:
        # 获取所有课程列表
        course_list = teacher_interface.get_all_course('course')
        if not course_list:
            print("没有课程可选！")
            return
        print('=' * 30)
        for index, course in enumerate(course_list):
            print('编号：%s  课程：%s' % (index, course))
        print('=' * 30)
        choice = input("请选择教授的课程编号：")
        if not choice.isdigit():
            print("请输入数字！")
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(course_list)):
            print("请输入合法编号！")
            continue
        course_name = course_list[choice]
        flag, msg = teacher_interface.choose_course_interface(teacher_info['name'], course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth('teacher')
def check_student_in_course():
    print("查看课程下的学生界面".center(30, '-'))
    while True:
        # 获取所授课程
        flag, course_list = teacher_interface.check_course_interface(teacher_info['name'])
        if not flag:
            print(course_list)
            break
        print('=' * 30)
        for index, course in enumerate(course_list):
            print('编号：%s  课程：%s' % (index, course))
        print('=' * 30)
        choice = input("请输入课程编号：")
        if not choice.isdigit():
            print("请输入数字！")
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(course_list)):
            print("请输入合法编号！")
            continue
        course_name = course_list[choice]
        msg = teacher_interface.check_student_interface(teacher_info['name'], course_name)
        if not msg:
            print("课程下没有学生！")
            break
        print(msg)
        break


@common.login_auth('teacher')
def modify_score_of_student():
    '''
    1、打印老师下面的所有课程
    2、选择某一门课程下的某个学生，打印
    3、设置成绩
    '''
    print("修改分数界面".center(30, '-'))
    while True:
        # 获取所授课程
        flag, course_list = teacher_interface.check_course_interface(teacher_info['name'])
        if not flag:
            print(course_list)
            break
        print('=' * 30)
        for index, course in enumerate(course_list):
            print('编号：%s  课程：%s' % (index, course))
        print('=' * 30)
        choice = input("请输入课程编号：")
        if not choice.isdigit():
            print("请输入数字！")
            continue
        choice = int(choice)
        if not (choice >= 0 and choice < len(course_list)):
            print("请输入合法编号！")
            continue
        course_name = course_list[choice]
        student_list = teacher_interface.check_student_interface(teacher_info['name'], course_name)
        if not student_list:
            print("课程下没有学生！")
            break
        print('=' * 30)
        for i, student in enumerate(student_list):
            print('编号：%s  学生：%s' % (i, student))
        print('=' * 30)
        choose = input("请输入学生编号：")
        if not choose.isdigit():
            print("请输入数字！")
            continue
        choose = int(choose)
        if not (choose >= 0 and choose < len(student_list)):
            print("请输入合法编号！")
            continue
        student_name = student_list[choose]
        score = input("请输入分数：")
        flag, msg = teacher_interface.modify_score_interface(teacher_info['name'], student_name, course_name, score)
        if flag:
            print(msg)
            break


method_map = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_student_in_course,
    '5': modify_score_of_student
}


def teacher_view():
    print("欢迎来到老师视图！")
    while True:
        print('=' * 30)
        print('''
                1、登录
                2、查看教授的课程
                3、选择教授的课程
                4、查看课程下的学生
                5、修改学生的分数
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