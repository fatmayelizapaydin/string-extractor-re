# Temel python imajını kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Dosyaları kopyala
COPY . .

# Uygulamayı çalıştır
CMD ["python", "src/main.py"]
