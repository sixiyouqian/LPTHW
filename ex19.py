# encoding: utf-8
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30) # 直接调用函数


print "OR, we can use variables from our script:"
amount_of_cheese  = 10 # 变量赋值
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # 调用函数

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) # 完成计算，再调用函数

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100,
amount_of_crackers + 1000) #调用函数

def my_func(arg1=0):
    print str(arg1) + '\n'
    return arg1*arg1

print "way 1:"
my_func(1)
print "way 2:"
no = 1
my_func(no)
print "way 3:"
my_func(no + 1)
print "way 4:"
my_func(no - 1)
print "way 5:"
my_func()
print "way 6:"
my_func(1 + 2)
print "way 7:"
my_func(1 * 2)
print "way 8:"
my_func(my_func(1))
print "way 9:"
my_func(my_func(no))
print "way 10:"
my_func(my_func())
