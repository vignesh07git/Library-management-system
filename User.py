# -*- coding: utf-8 -*-





class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id


class Member(User):
    def __init__(self, name, location, age, aadhar_id, student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id

    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id

    # assume name is unique
    def issueBook(self, name, days=10):
        if days!=10:
            Print("first return the old book")
        else:
            print("You are eligible to take a book")
            catalog.removeBook()

    # assume name is unique
    def returnBook(self, name):
        catalog.addBook()
        print("Thanks and come again")


class Librarian(User):
    def __init__(self, name, location, age, aadhar_id, emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def __repr__(self):
        return self.name + self.location + self.emp_id

    def addBook(self, name, author, publish_date, pages):
        Catalog.addBook()

    def removeBook(self, name):
        Catalog.removeBook()

    def removeBookItemFromCatalog(self, book, isbn):
        Catalog.removeBookItem(book, isbn)