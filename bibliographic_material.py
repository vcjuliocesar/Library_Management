from abc import ABC,abstractclassmethod
from datetime import date

class BibliographicMaterial(ABC):
    
    @abstractclassmethod
    def __init__(self,title:str,author:str,published_year:date,topic:str) -> None:
        
        self._title = title.capitalize()
        
        self._author = author
        
        self._published_year = published_year
        
        self._topic = topic
    
    @abstractclassmethod    
    def rate(self,review:str):
        pass
    
    @property
    def title(self):
        
        return self._title
    
    @title.setter
    def title(self,title:str):
        
        self._title = title
        
    @property
    def author(self):
        
        return self._author
    
    @author.setter
    def author(self,author:str):
        
        self._author = author
        
    @property
    def published_year(self):
        
        return self._published_year
    
    @published_year.setter
    def published_year(self,published_year:date):
        
        self._published_year = published_year
        
    @property
    def topic(self):
        
        return self._topic
    
    @topic.setter
    def topic(self,topic:str):
        
        self._topic = topic
        
    @abstractclassmethod    
    def get_info(self):
        pass