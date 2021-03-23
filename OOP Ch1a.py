class Book():
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secrets = "This is secrets!"

    def get_price(self):
        if hasattr(self, "_discount"):  # * Note the attribute being tested is passed in as a string
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount

    def __repr__(self):
        return f"<Book title: {self.title}>"


b1 = Book("Automate Boring Stuff with Python", "Al", 300, 30)
print(b1)
b1.set_discount(0.25)
print(f"price = {b1.get_price()}")
print(b1._Book__secrets)
