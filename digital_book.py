from datetime import date

from bibliographic_material import BibliographicMaterial

class DigitalBook(BibliographicMaterial):
    
    def __init__(self, title: str, author: str, published_year: date,topic:str,format: str) -> None:
        
        super().__init__(title, author, published_year,topic)
        
        self.format = format
        
    def download(self):
        
        return f"Download book: {self.title} ..."
    
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
            Format : {self.format} \n 
        """