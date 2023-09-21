from datetime import date

from book import Book

from bibliographic_material import BibliographicMaterial

class DigitalBook(Book,BibliographicMaterial):
    
    def __init__(self, title: str, author: str, published_year: date,topic: str,format: str) -> None:
        
        Book.__init__(self,title, author, published_year)
        
        BibliographicMaterial.__init__(self,topic)
        
        self.format = format
        
    def download(self):
        
        return f"Download book: {self.title} ..."