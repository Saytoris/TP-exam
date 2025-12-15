# 1. Використовуємо чистий базовий образ Alpine (остання версія)
FROM alpine:latest

# 2. Встановлюємо робочу директорію
WORKDIR /app

# 3. ВСТАНОВЛЕННЯ СИСТЕМНИХ ЗАЛЕЖНОСТЕЙ
# apk — це пакетний менеджер Alpine (аналог apt в Ubuntu)
# --no-cache: не зберігати кеш завантажених файлів (зменшує розмір образу)
# Встановлюємо python3 та пакетний менеджер pip
RUN apk add --no-cache python3 py3-pip

# 4. Копіюємо файл залежностей
COPY requirements.txt .

# 5. ВСТАНОВЛЕННЯ БІБЛІОТЕК PYTHON
# --break-system-packages: ЦЕ ВАЖЛИВО для нових версій Alpine.
# Alpine захищає системний python від змін, але в Docker це безпечно,
# тому ми примусово дозволяємо встановлення пакетів глобально.
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# 6. Копіюємо код програми
COPY . .

# 7. Відкриваємо порт для веб-застосунку
EXPOSE 5000

# 8. Команда запуску за замовчуванням (Веб-сервер)
# Використовуємо python3 явно
CMD ["python3", "cli.py"]