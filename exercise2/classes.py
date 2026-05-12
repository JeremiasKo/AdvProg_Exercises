#!/usr/bin/env python3
# from os import name
class Person:
    name = 'John'
    age = 19
    classes = ['computer science', 'math', 'physics']
print(Person.name, Person.classes[1])

class Person2:
    def __init__(self, name, age, classes):
        self.name = name
        self.age = age
        self.classes = classes
person2 = Person2('Alice', 20, ['biology', 'chemistry'])
print(person2.name, person2.classes[0])