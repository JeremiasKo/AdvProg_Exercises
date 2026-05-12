import numpy as np

print("Hello World")
some_list = [1, 2, 3, 4, 5]
try:
    item = some_list[10]
except IndexError:
    print("Index out of range")
    
some_list = [1, 2, 3, 4, 5]
try:
    item = some_list[10]
except: # general exceptions
    a=0
some_list = [1, 2, 3, 4, 5]
try:
    item = some_list[10]
except Exception as err: # to know what error it was 
    print(err)
    
try:
    item = some_list[10]
except ValueError: # to know what error it was 
    print('Value error occurred')
except IndexError: # to know what error it was 
    print('Index error occurred')
finally: # this is alwys executed
    print('this runs')
    