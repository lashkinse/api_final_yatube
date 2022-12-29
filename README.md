# API для Yatube

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

## Описание

Итоговый проект в рамках курса "Python-разработчик". Спринт 9. API для Yatube.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/lashkinse/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Документация для API

```
http://127.0.0.1:8000/redoc/
```

## Примеры запросов к API

### Получение публикаций

Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.

GET-запрос:

```
http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4
```

Ответ:

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### Создание публикации

Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

POST-запрос:

```
http://127.0.0.1:8000/api/v1/posts/
```

Тело запроса:

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Ответ:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Получение публикации

Получение публикации по id.

GET-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Ответ:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Обновление публикации

Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.

PUT-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Тело запроса:

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Ответ:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Частичное обновление публикации

Частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.

PATCH-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Тело запроса:

```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Ответ:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

### Удаление публикации

Удаление публикации по id. Удалить публикацию может только автор публикации. Анонимные запросы запрещены.

DELETE-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

### Получение комментариев

Получение всех комментариев к публикации.

GET-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Ответ:

```json
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

### Добавление комментария

Добавление нового комментария к публикации. Анонимные запросы запрещены.

POST-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Тело запроса:

```json
{
  "text": "string"
}
```

Ответ:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Получение комментария

Получение комментария к публикации по id.

GET-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Ответ:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Обновление комментария

Обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы
запрещены.

PUT-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Тело запроса:

```json
{
  "text": "string"
}
```

Ответ:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Частичное обновление комментария

Частичное обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные
запросы запрещены.

PATCH-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Тело запроса:

```json
{
  "text": "string"
}
```

Ответ:

```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

### Удаление комментария

Удаление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы
запрещены.

DELETE-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

### Список сообществ

Получение списка доступных сообществ.

GET-запрос:

```
http://127.0.0.1:8000/api/v1/groups/
```

Ответ:

```json
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```

### Информация о сообществе

Получение информации о сообществе по id.

GET-запрос:

```
http://127.0.0.1:8000/api/v1/groups/{id}/
```

Ответ:

```json
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```

### Подписки

Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.

POST-запрос:

```
http://127.0.0.1:8000/api/v1/follow/
```

Тело запроса:

```json
{
  "following": "string"
}
```

Ответ:

```json
{
  "user": "string",
  "following": "string"
}
```

### Получить JWT-токен

Получение JWT-токена.

POST-запрос:

```
http://127.0.0.1:8000/api/v1/jwt/create/
```

Тело запроса:

```json
{
  "username": "string",
  "password": "string"
}
```

Ответ:

```json
{
  "refresh": "string",
  "access": "string"
}
```

### Обновить JWT-токен

Обновление JWT-токена.

POST-запрос:

```
http://127.0.0.1:8000/api/v1/jwt/refresh/
```

Тело запроса:

```json
{
  "refresh": "string"
}
```

Ответ:

```json
{
  "access": "string"
}
```

### Проверить JWT-токен

Проверка JWT-токена.

POST-запрос:

```
http://127.0.0.1:8000/api/v1/jwt/verify/
```

Тело запроса:

```json
{
  "token": "string"
}
```
