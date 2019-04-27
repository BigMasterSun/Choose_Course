# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:39

from db import db_handler


class Base:

    def save(self):
        db_handler.db_save(self)

    @classmethod
    def select(cls, name):
        obj = db_handler.db_select(cls,name)
        return obj


class Admin(Base):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    def create_teacher(self, teacher_name, teacher_pwd):
        Teacher(teacher_name, teacher_pwd)

    def create_course(self, course_name):
        Course(course_name)

    def create_school(self, school_name, school_address):
        School(school_name, school_address)


class Student(Base):
    def __init__(self, student_name, student_pwd):
        self.name = student_name
        self.pwd = student_pwd
        self.student_course_list = []
        self.score = {}
        self.school = None
        self.save()

    def choose_school(self, school_name):
        self.school = school_name
        self.save()

    def choose_course(self,course_name):
        self.student_course_list.append(course_name)
        self.score[course_name] = 0
        self.save()

    def check_score(self,course_name):
        return self.score[course_name]


class Teacher(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.name = teacher_name
        self.pwd = teacher_pwd
        self.teacher_course_list = []
        self.save()

    def check_course(self):
        return self.teacher_course_list

    def choose_course(self, course_name):
        self.teacher_course_list.append(course_name)
        self.save()

    def check_student_in_course(self, course_name):
        course_obj = Course.select(course_name)
        return course_obj.course_student_list

    def modify_score_of_student(self, student_name, course_name, score):
        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()


class School(Base):
    def __init__(self, school_name, school_address):
        self.name = school_name
        self.school_address = school_address
        self.school_course_list = []
        self.save()
    def add_course(self,course_name):
        self.school_course_list.append(course_name)
        self.save()


class Course(Base):
    def __init__(self, course_name):
        self.name = course_name
        self.course_student_list = []
        self.save()

    def add_student(self,student_name):
        self.course_student_list.append(student_name)
        self.save()
