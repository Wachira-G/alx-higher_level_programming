#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())

try:
    d = Square("13")
    print(d)
    print(d.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
