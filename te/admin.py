# #from django.contrib import admin
#
# # 1
# a = 4
# if a == 0 or a < 0:
#     print(False)
# else:
#     print(True)
#
# # 2
# a = 1234
# b = a % 2
# if b == 0:
#     print('Четное')
# else:
#     print('Нечетное')
#
#     #3
# a = 400
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print('visokosniy')
# else:
#     print('nevisokostniy')
#
    #4
# a = input()
# b = int(input())
#
# for i in range(b):
#     print(a)

     #5
a = int(input())
b = int(input())
op = str(input())
if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
    print(f'{a} {op} {b}')
elif op == '/':
    result = a / b
print(f"{a} {op} {b} = {result}")





# i = 0
# while i < 5:
#     i += 1
#     if i == 5:
#         print(i)
#
#

# numbers = [3,4,5,6,7]
# a = min(numbers)
# q = numbers.remove(a)
#
# print(q)
