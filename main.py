from book import Book
from physical_book import PhysicalBook
from digital_book import DigitalBook

def run():
    b = Book("Harry Potter and the Philosopher's Stone","J.K. Rowling",1997)
    pbook = PhysicalBook("Harry Potter and the Philosopher's Stone","J.K. Rowling",1997,"A-32")
    pbook.lend()
    pbook.give_back()
    print(pbook.get_info())
    
    dbook = DigitalBook("Harry Potter and the Philosopher's Stone","J.K. Rowling",1997,"PDF")
    print(dbook.download())

if __name__ == "__main__":
    run()