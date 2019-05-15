# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:40:39 2019

@author: Stefan Draghici
"""

class Employee:
    def set_working_hours(self):
        self.working_hours=40
        
    def display_working_hours(self):
        print(self.working_hours)
        
        
class Trainee(Employee):
    def set_working_hours(self):
        self.working_hours=20
        
    def reset_working_hours(self):
        super().set_working_hours()
        
        
        
e=Employee()
e.set_working_hours()
e.display_working_hours()

t=Trainee()
t.set_working_hours()
t.display_working_hours()
t.reset_working_hours()
t.display_working_hours()