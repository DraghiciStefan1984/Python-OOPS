# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:32:18 2019

@author: Stefan Draghici
"""

class Car:
    #class attributes
    engine='diesel'
    
    def __init__(self, make, model, fuel):
        #instance attributes
        self.make=make
        self.model=model
        self.fuel=fuel
        
    def start(self):
        print('Car starts.')
        
    def stop(self):
        print('Car stops.')
        
    def brake(self):
        print('Car hit the brakes.')
        
    def honk(self, sound):
        print('Car is honking: ', sound)
        
    def change_engine(self, engine):
        self.engine=engines
        
        
class Jeep(Car):
    def mode4x4(self):
        print('4 x 4.')
        
car1=Car('Mercedes', 'S 500', 3500)
car2=Car('BMW', 'Series 300', 1500)
car1.start()
car1.brake()
car2.stop()
car2.honk('tiiiiit!!!!')
car3=Jeep('Toyota', 'Hillux', 4500)
car3.mode4x4()