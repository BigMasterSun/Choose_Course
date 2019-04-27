# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:38

def login_auth(user_type):
    from core import admin, student, teacher
    def wrapper(fn):
        def inner(*args, **kwargs):
            if user_type == 'admin':
                if not admin.admin_info['name']:
                    print("当前未登录，请先登录！")
                    admin.login()
                res = fn(*args, **kwargs)
                return res
            elif user_type == 'student':
                if not student.student_info['name']:
                    print("当前未登录，请先登录！")
                    student.login()
                res = fn(*args, **kwargs)
                return res
            elif user_type == 'teacher':
                if not teacher.teacher_info['name']:
                    print("当前未登录，请先登录！")
                    teacher.login()
                res = fn(*args, **kwargs)
                return res
        return inner
    return wrapper
