#!/bin/sh
# Start Uvicorn processes
echo "Starting Uvicorn."

# Получаем порт из переменной окружения, если она не установлена — используем дефолтный 8000
PORT=${APP_PORT:-8000}

# Running Uvicorn server
exec uvicorn src.infrastructure.api.app:create_app --host 0.0.0.0 --port $PORT --workers 1 --proxy-headers --factory
