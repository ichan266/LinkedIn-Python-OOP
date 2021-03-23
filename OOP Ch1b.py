class Book:

    # $ Class Methods: This creates a property that applies to all instances of the Book class
    BOOK_TYPE = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # @ Static Methods: Double-underscores properties are hidden from other classes
    __booklist = None

    def __init__(self, title, book_type):
        self.title = title
        # * BOOK_TYPE is a class attribute. So to get access to the tuple, BOOK_TYPE, we use Book.BOOK_TYPE
        if (not book_type in Book.BOOK_TYPE):
            raise ValueError(f"{book_type} is not a valid BOOK_TYPE")
        else:
            self.book_type = book_type

    def set_title(self, new_title):
        self.title = new_title

    # $ Class Method
    @classmethod
    def get_book_type(cls):  # * this works on a class instance (not an object instance)
        return cls.BOOK_TYPE

    # @ Static Method
    @staticmethod
    def get_booklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def __repr__(self):
        return f"<Book title: {self.title}>"


class Newspaper:
    def __init__(self, name):
        self.name = name


b1 = Book("Make It Stick", "HARDCOVER")
b2 = Book("In My Own Words", "EBOOK")
n1 = Newspaper("New York Times")
n2 = Newspaper("Washington Post")

print("Book types are", Book.get_book_type())

thebooks = Book.get_booklist()
thebooks.append(b1)
thebooks.append(b2)

print(thebooks)
