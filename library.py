from typing import Optional
from library.model.book import Book
from library.model.genre import Genre


class Library():

    # Prints crime audio books
    def print_longest_crime_audio_book(self) -> str:
        crime_audio_books: list[Book] = []
        max: Optional[Book] = None

        # print banner
        print("*********************************************")
        print("********* Longest Crime Audio Book **********")
        print("*********************************************")

        for b in self.get_books():
            if Genre.CRIME in b.genres:
                if b._book_type == "Audio":
                    if max is not None and max.duration < b.duration:
                        max = b
                    # end if
                # end if
            else:
                pass
            # end else
        # end for

        print(f"Title: {max.title}")
        print(f"Author: {max.authors}")
        print(f"Duration: {max.duration}")
        print(f"______________________________")
        return str(max)

    # Constructor
    def __init__(self, books: list[Book]):
        self._books = books

    _books: list[Book] = []

    def get_books(self) -> list[Book]:
        return self._books
