#!C:/Program Files/Python36/python.exe

'''
Created on Aug 22, 2017

@author: jlearx
'''
from datetime import date
 
if __name__ == '__main__':
    today = date.today()

    name = input("Please tell me your name: ")
    print("Your name is " + name)
    
    age = input("Please tell me your age: ")
    print("Your age is " + age)
    
    ageInt = int(age)
    diff = 100 - ageInt
    message = name + ", you will turn 100 years old in " + str(today.year + diff) + "."
    
    copies = input("Number of copies to print: ")
    
    for i in range(1,int(copies)+1):
        print(message)
