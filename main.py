from book import Book
from physical_book import PhysicalBook

def run():
    b = Book("Harry Potter and the Philosopher's Stone","J.K. Rowling",1997)
    pb = PhysicalBook("Harry Potter and the Philosopher's Stone","J.K. Rowling",1997,"A-32")
    pb.lend()
    #pb.give_back()
    print(pb.get_info())

if __name__ == "__main__":
    run()