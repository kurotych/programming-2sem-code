# Базовий образ
FROM python:3.13-slim

# Змінні для оптимізації Python в контейнері
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Робоча директорія
WORKDIR /app

# Спочатку копіюємо залежності (для кешування)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Потім копіюємо код
COPY . .

# Команда запуску
CMD ["python", "app.py"]
