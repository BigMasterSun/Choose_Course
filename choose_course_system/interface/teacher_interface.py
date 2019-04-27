# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:40
from db import models
from interface import common_interface


# 查看教授的课程
def check_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    course_list = teacher_obj.check_course()
    if not course_list:
        return False,'老师[%s]还没有选择教授的课程' % teacher_name
    return True,course_list


# 查看所有课程
def get_all_course(course):
    course_list = common_interface.check_all_file(course)
    if not course_list:
        return False
    return course_list


# 选择教授的课程
def choose_course_interface(teacher_name, course_name):
    teacher_obj = models.Teacher.select(teacher_name)
    if course_name in teacher_obj.teacher_course_list:
        return False,'已经选择过该课程了，请选择其他课程！'
    teacher_obj.choose_course(course_name)
    return True,'课程[%s]选择成功' % course_name


# 查看课程下的学生
def check_student_interface(teacher_name, course_name):
    teacher_obj = models.Teacher.select(teacher_name)
    student_list = teacher_obj.check_student_in_course(course_name)
    if not student_list:
        return False
    return student_list


# 修改分数接口
def modify_score_interface(teacher_name, student_name, course_name, score):
    teacher_obj = models.Teacher.select(teacher_name)
    teacher_obj.modify_score_of_student(student_name, course_name, score)
    return True,'分数修改成功！'

