class BibliographicMaterial:
    
    def __init__(self,topic:str) -> None:
        
        self.topic = topic
        
        self.review = None
        
    def rate(self,review:str):
        
        self.review = review
        
    def get_rate(self):
        
        return f"Review: {self.review}"