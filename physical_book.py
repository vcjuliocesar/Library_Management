from datetime import date
from book import Book

class PhysicalBook(Book):
    
    def __init__(self, title: str, author: str, published_year: date,location:str,state:str = "available") -> None:
        super().__init__(title, author, published_year)
        self.location = location
        self.state = state
        
    def lend(self):
        self.state = "loan"
    
    def give_back(self):
        self.state = "available"
        
    def get_info(self):
        return f"""
            Title : {self.title} \n
            Author : {self.author} \n
            Published year : {self.published_year} \n
            Location : {self.location} \n
            State : {self.state}            
        """