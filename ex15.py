# encoding: utf-8
from sys import argv # 引入argv
script, filename = argv # 将argv解包并赋给script和filename

txt = open(filename) # 打开文件返回一个file对象

print "Here's your file %r:" % filename
print txt.read(1) # file对象调用read函数，返回string对象
txt.close()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read(1)

txt_again.close()
