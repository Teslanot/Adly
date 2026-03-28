# Adly – Django веб-платформа для размещения объявлений

Добро пожаловать в мой первый Django-проект! Это современный сайт объявлений, где пользователи могут:

- Зарегистрироваться и войти в профиль
- Создавать объявления с изображениями
- Добавлять объявления в избранное
- Смотреть топ-пользователей по количеству объявлений
- Просматривать новые объявления за день и за неделю
-  Выходить из аккаунта и видеть свой ник

---

## ⚙️ Установка и запуск проекта

### 1. Клонировать репозиторий
```bash
git clone https://github.com/Teslanot/Adly.git
cd Adly
```

### 2. Создать и активировать виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

### 4. Настроить переменные окружения
Создайте .env файл и добавьте, например:
```ini
TOKEN=django token
EMAIL_USER=example@email.com
EMAIL_PASSWORD=aaaa bbbb cccc dddd
```

### 5. Выполнить миграции
```bash
python manage.py migrate
```

### 6. Собрать статику
```bash
python manage.py collectstatic
```

### 7. Запустить сервер
```bash
python manage.py runserver
```

---

## Публикация на продакшн (пример через Gunicorn + Nginx)
1. Настроить `settings.py`:
    - `DEBUG = False`
    - `ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']`

2. Установить Gunicorn:
```bash
pip install gunicorn
```

3. Запуск
```bash
gunicorn yourproject.wsgi:application --bind 0.0.0.0:8000
```

4. Настроить `nginx` и `supervisor` (опционально)

---

### 🛠 Будущие возможности (в разработке)

- Публичные профили для связи по объявлениям

- Привязка соцсетей (VK, Telegram и др.)

---

### Структура проекта
```csharp
adboard/
│
├── add/               # Приложение с объявлениями
├── auth/              # Регистрация и авторизация
├── main/              # Основная папка django
├── templates/         # HTML-шаблоны
├── static/            # Статические файлы (Tailwind CSS, JS)
├── media/             # Изображения пользователей и объявлений
├── manage.py          # Файл запуска
├── .env               # Файл с серетами 
└── ...
```

---

### Зависимости
- Python 3.10+
- Django 4.x+
- Pillow
- Tailwind CSS (через CLI или CDN)
- gunicorn (для деплоя)

Полный список — в requirements.txt.

---

### 📄 Лицензия
Этот проект распространяется под лицензией MIT. Это означает, что вы можете использовать, копировать, модифицировать и распространять код без ограничений, при условии сохранения оригинального авторства.

---

## 👤 Автор
Создан с нуля на Django ❤️
- Автор: Dan Aleks (Teslanot)
- GitHub: https://github.com/Teslanot

---

### Обратная связь
Если нашли баг или хотите предложить идею — создайте Issue или Pull Request.
