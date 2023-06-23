class Book:
    def __init__(self):
        self.price = 0
        self.ISBN = []
        
    def setPrice(self, price):
        self.price = price

    def set_from_book_branch_Price(self):
        return self.price
