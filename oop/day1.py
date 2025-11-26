#create a class book create its attributes

class Book():

    book_name = "To Kill a Mockingbird"
    def __init__(self, book_name, author, genre):
        self.book_name = book_name
        self.author = author
        self.genre = genre
        
    
    def get_details(self):
        return{
            "book_name" : self.book_name,
            "author_name": self.author,
            "genre": self.genre
        }
        

# book1 = Book("Harry Potter", 'JK.Rowling', "Fantasy")
# details = book1.get_details()
# print(book1.book_name)
# print(details)


#create a class movie create its attributes

class Movie():

    def __init__(self, title, genre):
        #private attribute
        #protected ko lagi single underscore
        #private ko lagi double underscore
        #this is the exmaple of encapsulation
        self.__title = title
        self.__genre = genre

    #getter and setter
    def get_details(self):
        return f"Title: {self.__title}, Genre: {self.__genre}"

    def set_details(self,new_title, new_genre):
        self.__title = new_title
        self.__genre = new_genre



# movie1 = Movie("Inception", "Sci-Fi")
# # print(movie1.title)
# #when we try to access this private attribute it will throw an error
# #getter ra setter use garna parcha to access and modify private attribute
# print(movie1.get_details())
# movie1.set_details("Avatar", "Sci-Fi")
# print(movie1.get_details())


#child class of the Movie class inheritance ko example
class Hollywood(Movie):
    def __init__(self, title, genre, director, rating):
        #parent class ko constructor call gareko
        super() .__init__(title,genre)
        self.director = director
        self.rating = rating
    #example of method overriding and polymorphism
    def get_details(self):
        parent_details = super().get_details()
        return f"{parent_details}, Director: {self.director}, Rating: {self.rating}"



obj1 = Hollywood("Inception", "Sci-Fi", "Christopher Nolan", "8.8")
print(obj1.get_details())