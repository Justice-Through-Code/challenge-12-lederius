from multiprocessing import AuthenticationError
#from turtle import title
from book import Book


class Library():
    def __init__(self):
        self.books = []
        """Initialize the empty book list"""
        

    def add_title(self, title: str, author: str):
        self.title = title
        self.author = author
        new_book = Book(title, author)
        self.books.append(new_book)
        """Add a Book object with the given title and author to the book list"""
        

    def count_books(self):
        """Return the number of books currently in the booklist"""
        return len(self.books)
        

    def remove_title(self, title:str):
        """Remove a book from the book list"""
        self.title = title
        #print(f'title passed --> {self.title}')

        # for x in range(len(self.books)):
        #     print(f'just x -->{x}')
        #     print(f'just self.books[x] -->{self.books[x]}')
        #     print(f'just self.books[x][title] -->{self.books[x][title]}')
        #     # if x[title] == self.title:
        #     #     print('match!!!')
                

        for bookTitle in self.books:
            #print(f'just book title -->{bookTitle}')
            #print(f'book title --> {bookTitle.title}')
            if bookTitle.title == self.title:
                # print('match!!!', )
                # print(f'self.books --> {self.books}')
                # print(f' will this work --> {self.books[bookTitle]}')
                self.books.remove(bookTitle)
                #spent HOURS trying to get line 43 to work so it could help
                # me figure out the issue with line 44
                # just to realize line 43 wont wokr but line 44 does what i need
        
        

    def is_empty(self):
        """Return True if the book list is empty, False if not"""
        return self.books == []

    def display_books(self):
        # print(f'presorted --> {self.books}')
        self.books.sort()
        # print(f'sorted --> {self.books}')
        for book in self.books:
            print(book)
