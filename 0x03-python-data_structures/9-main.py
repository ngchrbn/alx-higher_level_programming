#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
my_list_1 = []
my_list_2 = [1, 30]
max_value = max_integer(my_list)
max_value1 = max_integer(my_list_1)
max_value2 = max_integer(my_list_2)
print("Max: {}".format(max_value))
print("Max: {}".format(max_value1))
print("Max: {}".format(max_value2))
