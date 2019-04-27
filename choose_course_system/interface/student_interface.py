# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:40
from db import models
from . import common_interface


# 注册接口
def register_interface(name, pwd):
    student_obj = models.Student.select(name)
    if student_obj:
        return False,'学生[%s]已存在' % name
    models.Student(name, pwd)
    return True,'学生[%s]注册成功' % name


# 获取所有可选的学校
def get_all_school(school):
    school_list = common_interface.check_all_file(school)
    if not school_list:
        return False
    return school_list


# 选择学校
def choose_school_interface(student_name, school_name):
    student_obj = models.Student.select(student_name)
    if student_obj.school:
        return False,'学生[%s]已选择过学校' % student_name
    student_obj.choose_school(school_name)
    return True,'学生[%s]选择学校成功' % student_name


# 查看学生所选学校
def get_school(student_name):
    student_obj = models.Student.select(student_name)
    if not student_obj.school:
        return False
    return student_obj.school


# 查看某学校所有可选的课程
def get_all_course(school_name):
    school_obj = models.School.select(school_name)
    if not school_obj.school_course_list:
        return False
    return school_obj.school_course_list


# 选课接口
def choose_course_interface(student_name, course_name):
    student_obj = models.Student.select(student_name)
    if course_name in student_obj.student_course_list:
        return False,'课程[%s]已存在，无需再选' % course_name
    student_obj.choose_course(course_name)
    course_obj = models.Course.select(course_name)
    course_obj.add_student(student_name)
    return True,'选课成功，课程名：%s' % course_name


# 查看所选的课程
def get_student_course(student_name):
    student_obj = models.Student.select(student_name)
    if not student_obj.student_course_list:
        return False
    return student_obj.student_course_list


# 查看分数
def get_score_interface(student_name, course_name):
    student_obj = models.Student.select(student_name)
    score = student_obj.check_score(course_name)
    return score