#lms (library management system)
import json

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"Title: {self.name} , Author: {self.author},  Book Pages: {self.pages}"




class EBook(Book):
    def __init__(self, name, author, pages, filesize):
        super().__init__(name, author, pages)
        self.filesize = filesize

    def __str__(self):
        return f"Title: {self.name} , Author: {self.author},  Book Pages: {self.pages}, File Size: {self.filesize}MB"
    
    

class LMS:
    def __init__(self, book: object):
        self.book = book         
    
    def add_book(self):
        if  isinstance(self.book, EBook):
            self.book_dict = {
                "name": self.book.name,
                "author": self.book.author,
                "pages": self.book.pages,
                "filesize": self.book.filesize
            }
            
        elif isinstance(self.book, Book):
            self.book_dict = {
                "name": self.book.name,
                "author": self.book.author,
                "pages": self.book.pages
            }
        with open ('books_database', "a") as f:
            json.dump(self.book_dict,f)
            f.write("\n")
    
    def load_book(self):
        self.books_list=[]
        with open('books_database', 'r') as f:
            for line in f.read().splitlines():
                self.books_list.append(json.loads(line))
        return self.books_list
            
    
    def search_book(self, name):
        self.load_book()
        for book in self.books_list:
            if book['name'] == name:
                return book
        return None
    
    
    def delete_book(self,name):
        found = self.search_book(name)
        if found is None:
            return f"{name} not found "

        self.load_book()
        self.books_list = [book for book in self.books_list if book["name"]!= name]
        
        with open('books_database', 'w') as f:
            for book in self.books_list:
                json.dump(book,f)
                f.write("\n")
        return f"{name} deleted successfully"

if __name__ == "__main__":
 
    b1 = Book("Harry Potter", "J.K. Rowling", 500)
    b2 = Book("The Alchemist", "Paulo Coelho", 200)
    eb1 = EBook("Digital Fortress", "Dan Brown", 350, 5)
    eb2 = EBook("Dune", "Frank Herbert", 400, 10)

  
    lms1 = LMS(b1)
    print("Adding:", b1)
    lms1.add_book()

    lms2 = LMS(b2)
    print("Adding:", b2)
    lms2.add_book()

    lms3 = LMS(eb1)
    print("Adding:", eb1)
    lms3.add_book()

    lms4 = LMS(eb2)
    print("Adding:", eb2)
    lms4.add_book()

    print("\nLoad books")
    lms_all = LMS(None)  
    books = lms_all.load_book()
    for book in books:
        print(book)

    print("\nSearching  book")
    search_name = "Digital Fortress"
    result = lms_all.search_book(search_name)
    if result:
        print(f"Found: {result}")
    else:
        print(f"{search_name} not found")

    print("\nDeleting  book")
    delete_name = "The Alchemist"
    print(lms_all.delete_book(delete_name))

    print("\nBooks after deleting")
    books_after = lms_all.load_book()
    for book in books_after:
        print(book)
