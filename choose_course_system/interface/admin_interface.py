# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:39
from db import models


# 注册接口
def register_interface(name, pwd):
    # admin对象
    admin_obj = models.Admin.select(name)
    if admin_obj:
        return False,'管理员用户[%s]已存在' % name
    # 调用类，自动触发内部__init__的执行
    models.Admin(name, pwd)
    return True,'管理员用户[%s]创建成功' % name


# 创建学校接口
def create_school_interface(admin_name, school_name, school_address):
    school_obj = models.School.select(school_name)
    if school_obj:
        return False,'学校[%s]已存在' % school_name
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_school(school_name, school_address)
    return True,'学校[%s]创建成功' % school_name


# 创建老师接口
def create_teacher_interface(admin_name, teacher_name, teacher_pwd='123'):
    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj:
        return False,'老师[%s]已存在' % teacher_name
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True,'老师[%s]创建成功' % teacher_name


# 创建课程接口
def create_course_interface(admin_name, school_name, course_name):
    school_obj = models.School.select(school_name)
    if course_name in school_obj.school_course_list:
        return False,"课程[%s]已经存在" % course_name
    admin_obj = models.Admin.select(admin_name)
    admin_obj.create_course(course_name)
    school_obj.add_course(course_name)
    return True,"课程[%s]创建成功" % course_name
