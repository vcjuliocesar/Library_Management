from datetime import date

from book import Book

from bibliographic_material import BibliographicMaterial

class PhysicalBook(Book,BibliographicMaterial):
    
    def __init__(self, title: str, author: str, published_year: date,topic:str,location:str,state:str) -> None:
        
        Book.__init__(self,title, author, published_year)
        
        BibliographicMaterial.__init__(self,topic)
        
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
    
    def get_info(self):
        
        return f"""
            Title : {self.title} \n
            Author : {self.author} \n
            Published year : {self.published_year} \n
            Topic: {self.topic} \n
            Location : {self.location} \n
            State : {self.state}            
        """