# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:40

from db import models
from conf import settings
import os


# 查看某文件夹下所有文件
def check_all_file(user_type):
    path = os.path.join(settings.DB_PATH, user_type)
    if not os.path.exists(path):
        return False
    return os.listdir(path)


# 公共登录接口
def login_interface(name,pwd,role):
    if role == 'admin':
        obj = models.Admin.select(name)
        if not obj:
            return False, '管理员用户[%s]不存在' % name
    elif role == 'student':
        obj = models.Student.select(name)
        if not obj:
            return False,'学生[%s]不存在' % name
    elif role == 'teacher':
        obj = models.Teacher.select(name)
        if not obj:
            return False,'老师[%s]不存在' % name
    else:
        return False,'没有权限！'
    if pwd == obj.pwd:
        return True,'[%s]登录成功' % name
    return False,'密码错误！'