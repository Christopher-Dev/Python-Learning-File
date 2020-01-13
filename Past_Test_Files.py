print('Hello World')
#Introductions to variables
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



#-----------------------------------------------------------------------------------------
#Functions
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

def function5(some_argument):
    print(some_argument)
    print("weeeeeee")
function5(4)

#bmi function based calculator
name1 = "chris"
height_m1 = 2
weight_kg1 = 260

name2 = "austin"
height_m2 = 2
weight_kg2 = 155

name3 = "julia"
height_m3 = 1.4
weight_kg3 = 130

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print('bmi: ')
    print(bmi)
    if bmi < 25:
        return name + "not over weight"
    else:
        return name + " is over weight"
    
result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

#miles to kilometers converter

def calculator(x, y):
    return (x ** y)
a = calculator(5, 1.6)
print(a)


#--------------------------------------------------------------------------------------------

#introduction to Lists
a = [3, 10, -1]
print(a)
a.append(1)
print(a)
a.append("Hello")
print(a)
a.append([1, 2])
print(a)

#.pop always removes the last string from a list
#all lists go in square brackets "[]"
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)
a[0]
print(a[0])
a[2]
print(a[2])
#in python all lists start with 0 in the place of 1. Example- 0,1,2,3,4,5 instead of 1,2,3,4,5,6
#to replace a string in a list use "list name[define where you are replacing] = what you are replacing it with"
a[0] = 100
print(a)
#b = ([variable 1],[variable 2], [variable 3])
b = ["banana", "apple", "mirosoft"]
print(b)
#use the below method to move a variable around in a printed list
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)
#The method below is a quicker method used to move variables around in a printed list
b[0], b[2] = b[2], b[0]
print(b)
#-------------------------------------------------------------------------------------------
