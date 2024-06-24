# Онлайн Кошелек

Кошелек представляет собой систему управления электронным кошельком, разработанную на Django. Основные функции включают снятие средств, перевод средств между счетами и пополнение баланса.

## Инструкция по установке проекта

1. Спулить код с репозитория master.
2. Создать файл entrypoint.sh в директории app.
   1. Вставить в этот файл следующий код:
    ```
    #!/bin/sh

   if [ "$DATABASE" = "postgres" ]
   then
       echo "Waiting for postgres..."
   
       while ! nc -z $SQL_HOST $SQL_PORT; do
         sleep 0.1
       done
   
       echo "PostgreSQL started"
   fi
   
   python manage.py migrate
   python manage.py collectstatic --no-input --clear

   exec "$@"

    ```
   2. Если операционная система Mac или Linux прописать команду в терминале:
    ```
   chmod +x entrypoint.sh
    ```
3. Запустить сборку контейнеров командой:
```
docker-compose up -d --build
```
4. Затем нужно загрузить базовые данные которые подготовил. start.json.
```
docker-compose exec web python manage.py loaddata start.json
```
## Инструкция по использованию

Тестировать лучше всего с Postman.
Реализованы функционалы:
1. Снятие со счета "localhost:8000/api/v1/withdraw/" передаем json:
```
{
    "account_number": 987654321,
    "amount": 1000
}
```
2. Перевод с одного счета на другой "localhost:8000/api/v1/transfer/"
```
{
    "from_account_number": 123456789,
    "to_account_number": 987654321,
    "amount": 2000
}
```
3. Пополнение счета "localhost:8000/api/v1/deposit/"
```
{
    "account_number": 987654321,
    "amount": 5000
}
```

4. Админка "localhost:8000/admin/
   Login: user
   Password: 123
