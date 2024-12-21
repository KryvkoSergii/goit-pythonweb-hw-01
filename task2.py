from abc import ABC, abstractmethod
from typing import List
import logging

class Logger:
    def log(self, message: str):
        pass

class LoggerImpl(Logger):
    def __init__(self, logger_name: str):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)

        logger.addHandler(ch)

        self.logger = logger

    @abstractmethod
    def log(self, message: str):
        self.logger.info(message)

class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass

class Library(LibraryInterface):

    def __init__(self, logger: Logger):
        super().__init__()
        self.books: List[Book] = []
        self.logger: Logger = logger
    
    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break 

    def show_books(self):
        for book in self.books:
            self.logger.log(f'Title: {book.title}, Author: {book.author}, Year: {book.year}')

class LibraryManager:
    def __init__(self, libary: LibraryInterface):
        self.library:LibraryInterface = libary

    def add_book(self, title: str, author: str, year: str):
        self.library.add_book(Book(title, author, year))

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()

def main():
    logger = LoggerImpl('LibraryManager')
    library = Library(logger)
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.log("Invalid command. Please try again.")

if __name__ == "__main__":
    main()