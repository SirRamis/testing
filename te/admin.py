#from django.contrib import admin

# Register your models here.
a = 4
if a == 0 or a < 0:
    print(False)
else:
    print(True)


a = 1234
b = a % 2
if b == 0:
    print('Четное')
else:
    print('Нечетное')