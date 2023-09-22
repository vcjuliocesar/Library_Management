from datetime import date

class Book:
    
    def __init__(self,title:str,author:str,published_year:date) -> None:
        """_summary_
        encapsulation

        Args:
            title (str): _description_
            author (str): _description_
            published_year (date): _description_
        """
        self.__title = title.capitalize()
        
        self.__author = author
        
        self.published_year = published_year
        
    """_summary_
        getter
    Returns:
        str: title
    """
    @property
    def title(self):
        
        return self.__title
    
    """_summary_
    Returns:
        str: setter
    """
    @title.setter
    def title(self,title:str):
        
        self.__title = title
    
    @property
    def author(self):
        
        return self.__author
    
    @author.setter
    def author(self,author:str):
        
        self.author = author
            
    def get_info(self):
        
        return f"""
            Title : {self.title} \n
            Author : {self.author} \n
            Published year : {self.published_year} \n            
        """
    