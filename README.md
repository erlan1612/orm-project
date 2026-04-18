# Barbershop ORM Project

## 📌 Описание
Backend для барбершопа с использованием SQLAlchemy ORM и SQLite.

## 🧱 Модели
- Barber
- Client
- Appointment

## 🔗 Связи
- One-to-One: Client — Profile
- One-to-Many: Barber — Appointment
- Many-to-Many: Barber — Service

## 🚀 Запуск

```bash
pip install -r requirements.txt
python main.py