# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:12:36 2019

@author: Stefan Draghici
"""

class Apple:
    manufacturer='Apple Inc'
    contact_website='www.apple.com/contact'
    
    def contact_details(self):
        print('Contact us at ', self.contact_website)
        
        
class MacBook(Apple):
    def __init__(self):
        self.year_of_manufacture=2018
        
    def manufacture_details(self):
        print('This MacBook was manufactured in {0}, by {1}.'.format(self.year_of_manufacture, self.manufacturer))
        

macbook=MacBook()
macbook.manufacture_details()