from book import Book


def run():
    b = Book("Harry Potter and the Philosopher's Stone","J.K. Rowling",1997)
    
    print(b.get_info())

if __name__ == "__main__":
    run()