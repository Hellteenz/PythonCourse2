class Book:
    def __init__(self, id: int, name: str, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

        if not isinstance(id, int):
            raise TypeError("ID должен быть типа int")
        if id < 0:
            raise ValueError("ID должен быть неотрицательным числом")
        self.id = id

        if not isinstance(name, str):
            raise TypeError("Название должно быть типа str")
        if len(name) == 0:
            raise ValueError("Необходимо ввести название книги")

    def __str__(self):
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f'Book(id = {self.id}, name = \'{self.name}\', pages = {self.pages})'
