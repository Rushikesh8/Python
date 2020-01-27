# -*- coding: utf-8 -*-
from datetime import datetime,timedelta
class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        self.issueRecord = {}
        self.issueTime = 0
        self.returnTime = 0
        
class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id,catalog):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        self.catalog = catalog
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self,name,days):
        self.days = days
        b2 = self.catalog.searchByName(name)
        
        obj = b2.searchBookItemByName(name)
        if obj.isbn:
            self.issueRecord.setdefault(name,obj)
            b2.removeBookItem(obj)
            self.issueTime = datetime.now()
            print("Book is Issued")
        else:
            print("Book is Not Available")
                
            
            
    #assume name is unique
    def returnBook(self,name):
        for key,value in self.issueRecord.items():
            if key == name:
                self.catalog.addBookItem(value.book,value.isbn,value.rack)
                print("The Book is Returned")
        self.issueRecord.pop(name)        
        self.returnTime = datetime.now()
        
        Time = self.returnTime - self.issueTime
        print(Time)
        
        if Time.days > self.days:
            f = Time.days - self.days
            fine = f * 2
            print("The Fine for Returned Book is {}".format(fine))
        else:
            print("No fine")
        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id,catalog):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        self.catalog = catalog
        
    def __repr__(self):
        return self.name + self.location + self.emp_id
    
    def addBook(self,name,author,publish_date,pages):
        self.catalog.addBook(self,name,author,publish_date,pages)
    
    def removeBook(self,name):
        for value in self.catalog.books:
            if value.name == name:
                self.catalog.books.remove(value)
        
        self.catalog.different_book_count -= 1
    
    def removeBookItemFromCatalog(self,catalog,name,isbn):
        b = catalog.searchByName(name)           # book object is return
        c = b.searchBookItem(isbn)               # bool item object is return
        b.removeBookItem(c)
        
        
    
    
        # -*- coding: utf-8 -*-

