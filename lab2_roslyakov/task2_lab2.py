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

# Класс Book
class Book:
    def __init__(self, id_, name, pages):
        """
        Конструктор класса Book.
        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Строковое представление книги
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Представление книги для разработки (валидный вызов конструктора).
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# Класс Library
class Library:
    def __init__(self, books=None):
        """
        Конструктор класса Library.
        :param books: Список книг, по умолчанию пустой
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """
        Возвращает следующий идентификатор книги.
        Если книг нет, возвращает 1.
        Если книги есть, возвращает идентификатор последней книги + 1.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        """
        Возвращает индекс книги в списке по её id.
        :param book_id: Идентификатор книги
        :return: Индекс книги в списке
        :raises ValueError: Если книги с таким id нет
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    # Инициализируем пустую библиотеку
    empty_library = Library()
    print(empty_library.get_next_book_id())  # Ожидаем: 1

    # Инициализируем библиотеку с книгами из BOOKS_DATABASE
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)

    print(library_with_books.get_next_book_id())  # Ожидаем: 3 (последний id 2, следующий 3)

    # Проверка метода get_index_by_book_id
    print(library_with_books.get_index_by_book_id(1))  # Ожидаем: 0 (индекс книги с id = 1)
    print(library_with_books.get_index_by_book_id(2))  # Ожидаем: 1 (индекс книги с id = 2)

    # Проверка вызова ошибки
    try:
        print(library_with_books.get_index_by_book_id(3))  # Книги с таким id нет
    except ValueError as e:
        print(e)  # Ожидаем сообщение: "Книги с запрашиваемым id не существует"
