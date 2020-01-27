# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

#b1 = Book('Shoe Dog','Phil Knight', '2015',312)
#b1.addBookItem('123mn','H1B2')
#b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123mn','H1B2')
catalog.addBookItem(b, '741bv','H1B4')
catalog.addBookItem(b, '159cx','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

b = catalog.addBook('Ikigai','Hector Garcia', '2017',208)
catalog.addBookItem(b, '951xz','M2N3')

catalog.displayAllBooks()


m1 = Member("John Doe","Mumbai",23,'zscgbjml','Python321',catalog)
print(m1.issueBook("Shoe Dog",5))
print(m1.issueRecord)

catalog.displayAllBooks()
print(m1.returnBook('Shoe Dog'))
print(m1.issueRecord)
catalog.displayAllBooks()
librarian = Librarian("Rushi","Bangalore",22,'qwerty','EdYoda',catalog) 
#print (m1)
#print (librarian)
librarian.removeBookItemFromCatalog(catalog,'Shoe Dog','123mn')
catalog.displayAllBooks()
librarian.removeBook('Moonwalking with Einstien')
catalog.displayAllBooks()