#!/usr/bin/env python3
# from os import name
class Person:
    name = 'John'
    age = 19
    classes = ['computer science', 'math', 'physics']
print(Person.name, Person.classes[1])

# class Person2:
#     def __init__(self, name, age, classes):
#         self.name = name
#         self.age = age
#         self.classes = classes1234
#     def check_class_validitiy(new_class):
#         # check if the class is valid
#         return True
#     def add_class(self, new_class):
#         if self.check_class_validitiy(new_class):
#             self.classes.append(new_class)
# person2 = Person2('Alice', 20, ['biology', 'chemistry'])
# person3 = Person2('Lena', 92, ['history', 'literature'])
# print(person2.name, person2.classes[0])
# person2.add_class('art')
# could also do:
# person2.classes.append('art')

class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin
    def deposit(self, amount):
        a = input('Enter pin: \n')
        if a == self.pin:
            self.balance += amount
    def withdraw(self, amount):
        a = input('Enter pin: \n')
        if a == self.pin:
            if self.balance >= amount:
                self.balance -= amount
        else:
            print('Insufficient funds')
account = BankAccount('Alice', 1000, 1234)
account.deposit(500)
account.withdraw(200)
print(account.name, account.balance)