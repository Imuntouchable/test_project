import json
import random

BOOKS_FILE = 'library.json'


class Library:
    def __init__(self):
        self.books = self.load_from_file()

    def load_from_file(self):
        """Загрузить данные из JSON-файла."""
        try:
            with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print('Создана база данных.')
            return []

    def save_to_file(self):
        """Сохранить данные в JSON-файл."""
        with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.books, f, ensure_ascii=False, indent=4)

    def generate_unique_id(self):
        """Генерирует уникальный 10-значный ID."""
        while True:
            unique_id = random.randint(1000000000, 9999999999)
            if not any(book['id'] == unique_id for book in self.books):
                return unique_id

    def add_book(self):
        """Добавить книгу с валидацией данных."""
        while True:
            title = input('Введите название книги: ').strip()
            if not title:
                print('Ошибка: Поле названия книги не может быть пустым.')
                continue
            break

        while True:
            author = input('Введите автора книги: ').strip()
            if not author:
                print('Ошибка: Поле автор книги не может быть пустым.')
                continue
            break

        while True:
            year_input = input('Введите год издания книги: ').strip()
            if not year_input.isdigit():
                print('Ошибка: Год издания должен быть положительным числом.')
                continue

            year = int(year_input)
            if year < 0 or year > 2024:
                print('Ошибка: Укажите реальный год издания (от 0 до 2024).')
                continue
            break

        new_book = {
            'id': self.generate_unique_id(),
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии',
        }
        self.books.append(new_book)
        self.save_to_file()
        print(f'Книга "{title}" успешно добавлена!')

    def delete_book(self):
        """Удалить книгу."""
        try:
            book_id = int(input('Введите ID книги для удаления: '))
            book = next(
                (book for book in self.books if book['id'] == book_id),
                None
            )
            if book:
                self.books.remove(book)
                self.save_to_file()
                print('Книга успешно удалена!')
            else:
                print('Книга с таким ID не найдена.')
        except ValueError:
            print('Ошибка: ID должен быть числом.')

    def search_books(self):
        """Поиск книг."""
        field = input(
            'По какому полю искать (title/author/year)? '
        ).strip().lower()
        query = input('Введите значение для поиска: ').strip()

        if field not in {'title', 'author', 'year'}:
            print('Некорректное поле для поиска.')
            return

        if field == 'year' and not query.isdigit():
            print('Ошибка: Год должен быть числом.')
            return

        if field == 'year':
            query = int(query)
            results = [book for book in self.books if book['year'] == query]
        else:
            results = [book for book in self.books if query.lower() in book[
                field
            ].lower()]

        if results:
            print(f"{'ID':<20} {'Title':<40} {'Author':<30} {'Year':<6} "
                  f"{'Status':<10}")
            for book in results:
                print(f"{book['id']:<20} {book['title']:<40} "
                      f"{book['author']:<30} {book['year']:<6} "
                      f"{book['status']:<10}")
        else:
            print('Книги не найдены.')

    def list_books(self):
        """Отобразить все книги."""
        if self.books:
            print('Список книг:')
            for book in self.books:
                print(f"{book['id']:<20} {book['title']:<40} "
                      f"{book['author']:<30} {book['year']:<6} "
                      f"{book['status']:<10}")
        else:
            print('Книг нет.')

    def update_status(self):
        """Изменить статус книги."""
        while True:
            try:
                book_id = int(input('Введите ID книги: '))
                book = next(
                    (book for book in self.books if book['id'] == book_id),
                    None
                )
                if not book:
                    print(f'Книга с ID {book_id} не найдена.')
                    continue

                current_status = book['status']
                print(f'Текущий статус книги с ID {book_id}: {current_status}')
                new_status = input(
                    'Введите статус ("в наличии" или "выдана"): '
                ).strip()
                if new_status not in {'в наличии', 'выдана'}:
                    print(
                        'Введите "в наличии" или "выдана".'
                    )
                    continue
                elif (
                    current_status == 'в наличии' and new_status == 'в наличии'
                ):
                    print('Книга уже находится в статусе "в наличии".')
                    continue
                elif current_status == 'выдана' and new_status == 'выдана':
                    print('Книга уже выдана.')
                    continue
                book['status'] = new_status
                self.save_to_file()
                print(f'Статус книги с ID {book_id} успешно обновлён!')
                break
            except ValueError:
                print('Ошибка: ID должен быть числом.')


class LibraryApp:
    def __init__(self):
        self.library = Library()

    def main_menu(self):
        """Главная функция приложения."""
        while True:
            print("\n" + "=" * 30)
            print("            МЕНЮ           ")
            print("=" * 30)
            print("  1. Добавить книгу")
            print("  2. Удалить книгу")
            print("  3. Искать книги")
            print("  4. Отобразить все книги")
            print("  5. Изменить статус книги")
            print("  6. Выйти")
            print("=" * 30)

            choice = input("Выберите действие (1-6): ").strip()
            print("=" * 30)

            if choice == "1":
                print("Добавление новой книги...")
                self.library.add_book()
            elif choice == "2":
                print("Удаление книги...")
                self.library.delete_book()
            elif choice == "3":
                print("Поиск книг...")
                self.library.search_books()
            elif choice == "4":
                print("Список всех книг:")
                self.library.list_books()
            elif choice == "5":
                print("Изменение статуса книги...")
                self.library.update_status()
            elif choice == "6":
                print("До свидания!")
                break
            else:
                print("Некорректный выбор. Попробуйте снова.")


if __name__ == '__main__':
    app = LibraryApp()
    app.main_menu()
