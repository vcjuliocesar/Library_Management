from datetime import date

from bibliographic_material import BibliographicMaterial

class PhysicalBook(BibliographicMaterial):
    
    def __init__(self, title: str, author: str, published_year: date,topic:str,location:str,state:str) -> None:
        
        super().__init__(title, author, published_year,topic)
        
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
    
    def rate(self,review:str):
        
        self.review = review
    
    def get_rate(self):
        
        return f"Review : {self.review}"
    
    def get_info(self):
        
        return f"""
            Title : {self.title} \n
            Author : {self.author} \n
            Published year : {self.published_year} \n
            Topic: {self.topic} \n
            Location : {self.location} \n
            State : {self.state} \n           
        """