from datetime import date

from book import Book

class DigitalBook(Book):
    
    def __init__(self, title: str, author: str, published_year: date,format:str) -> None:
        
        super().__init__(title, author, published_year)
        
        self.format = format
        
    def download(self):
        
        return f"Download book: {self.title} ..."