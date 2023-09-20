from datetime import date

from book import Book

class PhysicalBook(Book):
    
    def __init__(self, title: str, author: str, published_year: date,location:str,state:str) -> None:
        
        super().__init__(title, author, published_year)
        
        self.location = location
        
        self.state = state
        
    def lend(self):
        
        if self.state == "available":
            
            self.state = "loan"
        
            return "Successfully borrowed book"
        
        return "The book is not available at this time"
    
    def give_back(self):
        
        self.state = "available"
        
        return "Book returned successfully"