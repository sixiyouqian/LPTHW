# encoding: utf-8
def while_loop(numbers, lim=6, step=1):
    i= 0
    while i < lim:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i + step
        print "Numbers now: ",  numbers
        print "At the bottom i is %d" % i

def for_loop(numbers, lim=6, step=1):
    for i in range(0, lim, step):
        if i > 0:
            print "At the bottom i is %d" % i
        print "At the top i is %d" % i
        numbers.append(i)
        print "Numbers now: ",  numbers


numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#     i = i + 1
#     print "Numbers now: ",  numbers
#     print "At the bottom i is %d" % i

# while_loop(numbers, lim=6, step=1)
for_loop(numbers, lim=6, step=1)
print "The numbers:"

for num in numbers:
    print num
