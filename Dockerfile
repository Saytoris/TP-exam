# ЗМІНА: Використовуємо alpine (дуже легкий Linux)
FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

# Встановлюємо залежності
# (Для Flask цього достатньо, для складніших бібліотек типу pandas
# на alpine іноді треба встановлювати додаткові компілятори, але тут все ок)
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]