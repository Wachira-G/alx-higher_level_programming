#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

llist = [[1, 2, 3], 3, 4, 5]
print(llist)
new_lsit = copy_list(llist)

print(llist)
print(new_lsit)

print(new_lsit == llist)
print(new_lsit is llist)
