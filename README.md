# Django Project README

## Overview

This is a simple Django project that demonstrates how to create views, handle URL routing, and render HTML templates. The project includes routes for greeting users by name and displaying a welcome message.

## Features

- **Greeting Views**: Provides different greetings for specific names and a dynamic greeting based on user input.
- **HTML Templates**: Renders HTML templates using Django's template engine.
- **Admin Panel**: Includes a route to access Django's built-in admin panel.

## Project Structure

- **views.py**: Contains the logic for handling requests and returning responses.
- **urls.py**: Defines the URL patterns for the application.
- **templates/**: Directory for HTML templates.

### Views

1. **index**: Returns a simple text response "Hello!!!".
2. **misha**: Returns "Hello, Misha".
3. **david**: Returns "Hello, David".
4. **greet**: Returns a personalized greeting based on the name provided in the URL.
5. **html_doc**: Renders an HTML template (`index.html`).
6. **greet1**: Renders a greeting template (`greet.html`) with a name passed as a parameter.

### URL Patterns

- `/admin/`: Access the Django admin panel.
- `/hello/`: Base route for the hello app.
- `/hello/greet1/<name>/`: Dynamic greeting route.

### HTML Template (`greet.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hello!!</title>
</head>
<body>
    <h1>Hello, {{ name }}</h1>
    <p>Welcome to my page</p>
</body>
</html>
```

## How to Use

1. Clone the repository.
2. Install the required dependencies.
3. Run the Django server.
4. Access the routes via a web browser.

---

# README проекта Django

## Обзор

Это простой проект Django, который демонстрирует, как создавать представления, обрабатывать маршрутизацию URL и отображать HTML-шаблоны. Проект включает маршруты для приветствия пользователей по имени и отображения приветственного сообщения.

## Особенности

- **Представления приветствия**: Предоставляет различные приветствия для конкретных имен и динамическое приветствие на основе пользовательского ввода.
- **HTML-шаблоны**: Отображает HTML-шаблоны с использованием движка шаблонов Django.
- **Административная панель**: Включает маршрут для доступа к встроенной административной панели Django.

## Структура проекта

- **views.py**: Содержит логику обработки запросов и возврата ответов.
- **urls.py**: Определяет шаблоны URL для приложения.
- **templates/**: Директория для HTML-шаблонов.

### Представления

1. **index**: Возвращает простой текстовый ответ "Hello!!!".
2. **misha**: Возвращает "Hello, Misha".
3. **david**: Возвращает "Hello, David".
4. **greet**: Возвращает персонализированное приветствие на основе имени, указанного в URL.
5. **html_doc**: Отображает HTML-шаблон (`index.html`).
6. **greet1**: Отображает шаблон приветствия (`greet.html`) с именем, переданным в качестве параметра.

### Шаблоны URL

- `/admin/`: Доступ к административной панели Django.
- `/hello/`: Базовый маршрут для приложения hello.
- `/hello/greet1/<name>/`: Динамический маршрут приветствия.

### HTML-шаблон (`greet.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Hello!!</title>
</head>
<body>
    <h1>Hello, {{ name }}</h1>
    <p>Welcome to my page</p>
</body>
</html>
```

