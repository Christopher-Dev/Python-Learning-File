print ('bmi Calculator')
print('----------------------------------')

name = "Chris"
height_m = 2
weight_kg = 264

bmi = weight_kg / (height_m * height_m)
print('bmi: ')
print(bmi)
if bmi < 25:
    print('name')
    print ('is not over weight')
else:
    print('chris')
    print('is over weight')