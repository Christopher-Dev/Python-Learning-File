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
#for loops


a = ["banana", "apple", "ruby"]


print(a[0])
print(a[1])
print(a[2])
# very tedeious to repeat it
#use a "for loop instead :)"
#all functions, if-else statements, and for loops must end with a ":" or they will be undefined.

#loops

for element in a:
    print(element)
    print(element)
  
b = [20, 10, 5]
total = 0
for e in b:
    total = total + e
print(total)

#use a list range function to have the numbers listed instead of having to type out each one.
#range only gives the first number to second to last, example - range(1, 5) lists out 1,2,3,4 but not 5.
c = list(range(1,5))
print(c)
#to find the sum of a number use "total" = 0
total2 = 0
for i in range(1, 5):
    total2 += i
print(total2)

print(list(range(1, 8)))
# "%" is used for division.
total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total += i
print(total3)




#unsure of how to solve the problem...
print(list(range(1, 100)))

def printMultiples(1, 100):
    'takes n and m as integers and finds all first m multiples of n'
for m in (n,m):
    if n % 2 == 0:
        while n < 100:
            print(n)
#-----------------------------------------------------------------------------------------
#While loops


total2 = 0
j = 1
while j < 5:
    total2 += j
    j+= 1
print(total2)

total = 0
for i in range(1, 5):
    total += i
print(total)

given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total3 = 0
i = 0
while given_list[i] > 0:
    total3 += given_list[i]
    i += 1
print(total3)


total = 0
j = 1
while j < 5:
    total += j
    j += 1
print(total)
#-------------------------------------------------------------------------------------------------

for i in range(99, 0, -1):
    if i == 1:
        print('1 bottle of beer on the wall, 1 bottle of beer!')
        print('So take it down, pass it around, no more bottles of beer on the wall!')
    elif i == 2:
        print('2 more bottles of beer on the wall, 2 more bottles of beer!')
        print('So take one down, pass it around, 1 more bottle of beer on the wall!')
    else:
        print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
        print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))
#--------------------------------------------------------------------------------------------------------
def frange(start, stop, step):
     i = start
     while i < stop:
         yield i
         i += step

for i in frange(0.5, 1.0, 0.1):
    print(i)
#--------------------------------------------------------------------------------------------------------
#More For loops

a = ["apple", "banana", "republic"]
#the "a" is known as the variable, in this case "element"
#everything inside of the bracket is called a list
for element in a:
    print(element)
#this is a for loop, always start with the variable
for i in range(len(a)):
    print(a[i])
#when ever you use the range function it will start from #0, 1, 2 which = to 0-3
#
#there are two ways of doing the same thing, problem one is simple and can be used in most cases, but sometimes the index
#^in this case, "i" the index matters and the second must be used to account for that.
#
#they both do exactly the dsame thing but just in two differant ways.

for i in range(len(a)):
    for j in range(i + 1):
        #i = 0 -> j = 0
        #i = 1 -> j = 0, 1
        #i = 2 -> j = 0, 1, 2
        print(a[i])
#so using the above method you can have i increase in prints
#tutorial 5 problem
print(list(range(1, 100)))
total = 0
for i in range(1, 100):
    if i % 3 == 0:
        total += i
    elif i % 5 == 0:
        total += i
print(total)

#or it can be added to the same line
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

#tutorial 6 problem
given_list =[7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
total2 = 0
j = len(given_list) - 1
while given_list[j] < 0:
    total2 += given_list[j]
    j -= 1
print(total2)
#-------------------------------------------------------------------------------------------------------
#Dictionary

d = {}
#to format the dictionary format as follows, d = {"George": 24, "Tom": 32} 
# this make the program think of it in a grid type of format, 24 and 32 are tha values while george and tom are the keys of the dictionary.
d["george"] = 24
d["tom"] = 32
d["jenny"] = 16
print(d["george"])
#when ever using a dictionary if you tell the program to print the key it will output the value ie. "george" would print out 24
#key are most often strings or numbers
d["jenny"] = 20
print(d["jenny"])
#a key can be changed at a later tmie by telling the dictionary to change it to a certain value given
#you can also add numbers as mentioned above to the dictionary just as strings
d["100"] = 10
print(d["100"])
#
#If you dont know how to do something *GOOGLE IT*
#Best resources are python discord-help areas and stackoverflow
#
for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")
#-----------------------------------------------------------------------------------------------------