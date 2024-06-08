# Инструкция по запуску сервиса
1. Склонировать репозиторий: git clone git@github.com:AytaDzhivanov1996/antipoff_tz.git
2. Создать вирт. окружение python3 -m venv env  и настроить перемнные окружения в .env-файле.
3. Применить миграции: docker compose run api python3 manage.py migrate
4. Запуск сервиса: docker compose up
5. Доступные эндпоинты находятся по адресу http://localhost:8000/swagger/