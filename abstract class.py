# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:26:38 2019

@author: Stefan Draghici
"""

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        return 0

class Square(Shape):
    side=4
    
    def area(self):
        return self.side*self.side
    
    
class Rectangle(Shape):
    width=5
    length=10
    
    def area(self):
        return self.width*self.length