from physical_book import PhysicalBook

from digital_book import DigitalBook

class User:
    
    def __init__(self,name:str,lastname:str) -> None:
        
        self.name  = name
        
        self.lastname = lastname
        
        self.library = []
        
    def borrowing(self,book:PhysicalBook | DigitalBook):
        
        self.library.append(book)
        
        return f"{book.title} has been added to your library"
    
    def give_back(self,book:PhysicalBook | DigitalBook):
        
        if book not in self.library:
        
            return f"You don't have the book {book.title} in your library"
        
        book.state = "available"
        
        return f"{book.title} has been returned"