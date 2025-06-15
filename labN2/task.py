class Book:
    """Класс для представления книги."""

    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация книги.

        Args:
            id_: идентификатор книги
            name: название книги
            pages: количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """Строковое представление для пользователя."""
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """Официальное строковое представление."""
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"