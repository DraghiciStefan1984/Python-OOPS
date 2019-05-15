# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:55:08 2019

@author: Stefan Draghici
"""

class Library:
    def __init__(self, book_list):
        self.book_list=book_list
        
    def display_available_books(self):
        for book in self.book_list:
            print(book)
    
    def lend_book(self, requested_book):
        if requested_book in self.book_list:
            print('You burrowed {}'.format(requested_book))
            self.book_list.remove(requested_book)
    
    def add_book(self, new_book):
        if new_book not in self.book_list:
            self.book_list.append(new_book)
    
    
class Customer:
    def request_book(self):
        print('What book would you like to burrow?')
        self.book=input()
        return self.book
    
    def return_book(self):
        print('What book would you like to return:')
        self.book=input()
        return self.book
    
    
library=Library(['Think and grow rich', 'Art of war', 'Computer Science'])
customer=Customer()

while(True):
    print('Enter 1 to display available books')
    print('Enter 2 to request a book')
    print('Enter 3 to return a book')
    print('Enter 4 to exit')
    user_choice=int(input())
    
    if user_choice==1:
        library.display_available_books()
    elif user_choice==2:
        requested_book=customer.request_book()
        library.lend_book(requested_book)
    elif user_choice==3:
        returned_book=customer.return_book()
        library.add_book(returned_book)
    elif user_choice==4:
        quit()