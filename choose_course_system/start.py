# -*- coding: utf-8 -*-
# @Author  : Sunhaojie
# @Time    : 2019/4/26 8:38

import os
import sys
from core import src
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    src.run()