# Library Management System

Это приложение для управления библиотекой книг. Оно позволяет добавлять, удалять, искать, отображать книги, а также изменять их статус. Данные хранятся в файле `library.json`, и при каждом изменении книги сохраняются автоматически.

## Функционал

### 1. Добавление книги
- Пользователь может добавить книгу в библиотеку, указав название, автора и год издания.
- Каждой книге автоматически присваивается уникальный 10-значный ID.
- Валидация данных:
  - Название книги не может быть пустым.
  - Автор книги не может быть пустым.
  - Год издания должен быть числом в пределах от 0 до 2024.

### 2. Удаление книги
- Пользователь может удалить книгу из библиотеки по её ID.

### 3. Поиск книг
- Возможность поиска книг по трем полям:
  - `title` (название)
  - `author` (автор)
  - `year` (год издания)
- Пользователь вводит поле и значение для поиска.
- Результаты поиска выводятся в виде списка книг с указанием ID, названия, автора, года издания и статуса.

### 4. Отображение всех книг
- Приложение выводит список всех книг в библиотеке, если таковые имеются.
- Для каждой книги отображаются ID, название, автор, год издания и статус.

### 5. Изменение статуса книги
- Пользователь может изменить статус книги на один из двух возможных:
  - `"в наличии"`
  - `"выдана"`
- Приложение проверяет, что текущий статус книги отличается от нового.
- Статус не может быть изменён на тот же самый.

### 6. Выход из приложения
- Пользователь может выйти из приложения, выбрав соответствующий пункт в меню.

## Структура данных

Все данные о книгах хранятся в JSON-файле `library.json`. Каждая книга представлена в виде словаря с ключами:
- `id` — уникальный идентификатор книги.
- `title` — название книги.
- `author` — автор книги.
- `year` — год издания книги.
- `status` — статус книги (в наличии/выдана).

Пример записи о книге:

```json
{
  "id": 1234567890,
  "title": "Война и мир",
  "author": "Лев Толстой",
  "year": 1869,
  "status": "в наличии"
}
