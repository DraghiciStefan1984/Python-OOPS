# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:39:13 2019

@author: Stefan Draghici
"""

class Employee:
    def __init__(self):
        self.name=''
        self.position=''
        
    @staticmethod
    def welcome_message():
        print('welcome to our organisation!')
        

Employee.welcome_message()
e1=Employee()
e1.name='John'
e1.position='Manager'
e1.welcome_message()