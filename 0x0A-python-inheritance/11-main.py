#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())

print('--------------------------')
try:
    s = Square()
except Exception as e:
    print(e)
print('--------------------------')

try:
    s = Square([12, 52])
except Exception as e:
    print(e)
print('--------------------------')

try:
    s = Square(-35)
except Exception as e:
    print(e)
print('--------------------------')

try:
    s = Square(0)
except Exception as e:
    print(e)
print('--------------------------')

s = Square(5)

try:
    print(s.width)
except Exception as e:
    print(e)
print('--------------')

try:
    print(s.height)
except Exception as e:
    print(e)
print('--------------')
