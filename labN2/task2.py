class Library:
    """Класс для представления библиотеки книг."""

    def __init__(self, books: list[Book] = None):
        """
        Инициализация библиотеки.

        Args:
            books: список книг (по умолчанию None)
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Получение ID для новой книги.

        Returns:
            Следующий доступный ID книги
        """
        return 1 if not self.books else self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Получение индекса книги по ID.

        Args:
            book_id: ID искомой книги

        Returns:
            Индекс книги в списке

        Raises:
            ValueError: если книга не найдена
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")