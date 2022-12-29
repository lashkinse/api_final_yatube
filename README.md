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
python3 -m pip install --upgrade pip
```
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

#### Получение публикаций

Получить список всех публикаций. При указании параметров **limit** и **offset** выдача должна работать с пагинацией.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4
```

Ответ:

```json
{
 
}
```

#### Получение публикации

Получение публикации по **id**.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{id}/
```

Ответ:

```json
{

}
```

#### Создание публикации

Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

**POST**-запрос:

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

}
```

#### Получение комментариев

Получение всех комментариев к публикации.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Ответ:

```json
[

]
```

#### Обновление комментария

Обновление комментария к публикации по **id**. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.

**PUT**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Ответ:

```json
{
}
```

#### Удаление комментария

Удаление комментария к публикации по **id**. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.

**DEL**-запрос:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

#### Список сообществ

Получение списка доступных сообществ.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/groups/
```

Ответ:

```json
[
  {
  }
]
```

#### Информация о сообществе

Получение информации о сообществе по **id**.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/groups/{id}/
```

Ответ:

```json
{
}
```

#### Подписки

Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.

**GET**-запрос:

```
http://127.0.0.1:8000/api/v1/follow/
```

Ответ:

```json
{
}
```

#### Получить JWT-токен

Получение JWT-токена.

**POST**-запрос:

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
}
```