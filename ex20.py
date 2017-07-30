# encoding: utf-8
from sys import argv

script, input_file = argv

def print_all(f):
    print f.read() # 读取文件中的所有内容

def rewind(f):
    f.seek(0) # 将文件的起始点设置成0

def print_a_line(line_count, f):
    print line_count, f.readline() # 读取文件游标当下的一行的数据，并游标下移一位

current_file = open(input_file)

print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)
