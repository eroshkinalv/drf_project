# Проект drf_project: платформа для онлайн-обучения

## Описание:

Проект drf_project - это учебный проект на Python, который представляет собой SPA веб-приложение. Результатом создания проекта будет бэкенд-сервер, который возвращает клиенту JSON-структуры.

Приложение online_courses:
- модель «Курс» (Course): название, превью (картинка), описание;
- модель «Урок» (Unit): название, превью (картинка), описание, ссылка на видео;

Приложение users:
- модель «Пользователь» (User): email, аватаз (картинка), телефон, страна;
- модель «Платеж» (Payment): пользователь, дата, курс/урок, сумма платежа, способ оплаты;

CRUD:
- модель «Курс» - Viewset
- модель «Урок» - Generic-классы
- модель «Пользователь» - Generic-классы
- модель «Платеж» - Viewset

Управление доступом:
- Модератор имеет право работы с любыми уроками и курсами, но без возможности их удалять и создавать новые.
- Пользователь может видеть, редактировать и удалять только свои курсы и уроки.
  
Другое:
- Настроена фильтрация для эндпоинтов вывода списка платежей
- Использована JWT-авторизация (каждый эндпоинт закрыт авторизацией)
  
## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/eroshkinalv/drf_project.git
```

## Документация:

Для получения дополнительной информации обратитесь к [папки с документацией пока нет](README.md).

## Лицензия:

Этот проект лицензирован по [лицензии](LICENSE.txt).
