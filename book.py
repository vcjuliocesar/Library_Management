from datetime import date

class Book:
    
    def __init__(self,title:str,author:str,published_year:date) -> None:
        self.title = title.capitalize()
        self.author = author.capitalize()
        self.published_year = published_year
        
        
    def get_info(self):
        return f"""
            Title : {self.title} \n
            Author : {self.author} \n
            Published year : {self.published_year} \n            
        """
    