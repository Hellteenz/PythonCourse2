from book import *


class Library:
    def __init__(self, books: list[Book] = []):
        self.books = books
        for i in range(len(books)):
            if not isinstance(books[i], Book):
                raise TypeError("Неверный тип входных данных")

    def get_next_book_id(self):
        if not self.books: return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, input_id: int):
        for i in range(len(self.books)):
            if input_id == self.books[i].id:
                return self.books.index(self.books[i])
            else: raise ValueError("Книги с запрашиваемым id не существует")