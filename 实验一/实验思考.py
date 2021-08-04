# 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入
import math
# 从模块中导入一个指定的部分到当前命名空间中
from math import fmod
# 把一个模块的所有内容全都导入到当前的命名空间
from math import *

unipath = u'~/你好.txt'
file = open(unipath, 'r')

binfile = open(unipath, 'rb')
