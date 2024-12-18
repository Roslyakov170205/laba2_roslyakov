BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]



class Book:
    def __init__(self, id_, name, pages):
        """
        Конструктор класса Book, инициализирует атрибуты:
        :param id_: Идентификатор книги (целое число)
        :param name: Название книги
        :param pages: Количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строку вида: Книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает строку, которая может использоваться для создания объекта Book.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


if __name__ == '__main__':
    
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    # Проверяем метод __str__
    for book in list_books:
        print(book)
