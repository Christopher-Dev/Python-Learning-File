
a = 1
b = 2


if a < b:
    print('b is greater than a')
    print('a is defenitly less than b')
print('Not sure if a is less than b')

c = 3
d = 4


if c < d:
    print('c is less than d')
else:
    print('c is greater than d')
print ('outside the if block')

e = 5
f = 6

if e < f:
    print('e is less than f')
elif e == f:
    print(' e is equal to f')
else:
    print('e is greater than f')



#Functions----------------------------------------------------------------

def function1():
    print('ahhhhhhh')
    print('ahhhhhhh 2')
print('This line is outside the function')


#a mapping
#input or an argument
def function2(x):
    return 2*x

a = function2(3)
print(a)
#when using a function call use print() or it wont return the answer.
#the part inside of the parentheses is called the argument. all def must have one or an error will occur.

def function3(x, y):
    return x + y
e = function3(5,7)
print(e)

def function4(x):
    print(x)
    print('this string still in the function')
    return 3*x
f = function4(4)
print(f)