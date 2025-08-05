# Социальная сеть для обмена фотографиями (Backend)

## Требования
- Python 3.10+
- PostgreSQL
- Django 5.0+
- DRF (Django REST Framework)

## Установка
1. Установите PostgreSQL и создайте БД (`dj_diplom`).
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/DSLykov/FinalWork.git
   cd social_network

## Создайте виртуальное окружение:
python -m venv venv

venv\Scripts\activate

## Установите зависимости:
pip install -r requirements.txt

## Настройте БД в settings.py:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dj_diplom",
        "USER": "adilet",
        "PASSWORD": "1",
    }
}

## Примените миграции:
python manage.py migrate

## Запустите сервер:
python manage.py runserver

## API Endpoints

- GET /api/posts/ – список постов (доступ без авторизации)
- POST /api/posts/ – создать пост (требуется токен)
- POST /api/posts/{id}/like/ – поставить/убрать лайк
- Полный список эндпоинтов: /api/
