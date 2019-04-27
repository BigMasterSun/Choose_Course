# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:39

import pickle
import os
from conf import settings


# 存
def db_save(obj):
    # 对象的类名作为文件夹名
    path = os.path.join(settings.DB_PATH, obj.__class__.__name__.lower())
    if not os.path.isdir(path):
        os.mkdir(path)
    # 每个类实例化的对象是不一样的，所以以对象名命名文件
    user_path = os.path.join(path, obj.name)
    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)
        f.flush()

# 取
def db_select(cls, name):
    # 传入的是类
    path = os.path.join(settings.DB_PATH, cls.__name__.lower())
    if not os.path.isdir(path):
        os.mkdir(path)
    user_path = os.path.join(path, name)
    if not os.path.exists(user_path):
        return False
    with open(user_path, 'rb') as f:
        obj = pickle.load(f)
        if obj:
            return obj
        return False