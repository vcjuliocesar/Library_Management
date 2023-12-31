from physical_book import PhysicalBook

from digital_book import DigitalBook

from user import User

def run():
    
    pbook = PhysicalBook("Harry Potter and the Philosopher's Stone","J.K. Rowling",1997,"Wizard","shelving-1","available")
    
    dbook = DigitalBook("The Lord of the Rings","J.R.R. Tolkien",1949,"Fantasy ","PDF")
    
    usr = User("Jhon","Doe")
    
    print(pbook.get_info())
    
    print(dbook.get_info())
    
    print(pbook.lend())
    
    print(usr.borrowing(pbook))
    
    print(usr.borrowing(dbook))
    
    print(usr.write_review(pbook,"It's a good book"))
    
    print(pbook.get_rate())
    
    print(pbook.lend())
    
    print(usr.give_back(pbook))
    
    print(pbook.lend())
    
    print(usr.borrowing(pbook))
    
    print(usr.give_back(pbook))
    
    print(dbook.download())
    
    

if __name__ == "__main__":
    
    run()
    
