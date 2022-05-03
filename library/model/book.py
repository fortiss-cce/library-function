import json

from datetime import datetime
from library.model.author import Author
from library.model.genre import Genre
from library.model.publisher import Publisher
import xml.etree.ElementTree as et


class Book:
    title: str
    authors: list[Author]
    publisher: Publisher
    publication_date: datetime
    genres: list[Genre]
    pages: int
    isbn: str

    existing_items: int
    borrowed_items: int

    _book_type: str
    duration: int = 0

    def __init__(self, title: str, authors, publisher, pub_date,  genres, pages, isbn, type, duration=0, existing_items=1, borrowed_items=0):
        self.title = title
        self.authors = authors
        self.publisher = publisher
        self.publication_date = pub_date
        self.genres = genres
        self.pages = pages
        self.isbn = isbn
        self._book_type = type
        self.duration = duration
        self.existing_items = existing_items
        self.borrowed_items = borrowed_items

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Book):
            return self.isbn == other.isbn and self._book_type == other._book_type
        return NotImplemented

    def __str__(self):
        return BookSerializer().serialize(self, "JSON")


class BookSerializer:
    def serialize(self, book: Book, format: str):
        if format == "JSON":
            book_info = {
                "id": book.isbn,
                "title": book.title,
                "authors": [author.get_fullname() for author in book.authors],
                "available_items": book.existing_items - book.borrowed_items,
                "borrowed_items": book.borrowed_items,
            }
            return json.dumps(book_info)
        elif format == "XML":
            book_info = et.Element("book", attrib={"id": book.isbn})
            title = et.SubElement(book_info, "title")
            title.text = book.title
            authors = et.SubElement(book_info, "authors")
            authors.text = ", ".join([author.get_fullname() for author in book.authors])
            avail = et.SubElement(book_info, "available")
            avail.text = str(book.existing_items - book.borrowed_items)
            authors = et.SubElement(book_info, "borrowed")
            authors.text = str(book.borrowed_items)
            return et.tostring(book_info, encoding="Unicode")
        else:
            raise ValueError(format)
