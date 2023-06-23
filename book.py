class Book:
    def __init__(self):
        self.price = 0
        self.ISBN = []
        
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price
