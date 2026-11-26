
# День 7
## Версия Python:
- VS Code: 3.12.7
- Docker: 3.12.3

## Dockerfile:
- FROM - выбор образа Python
- WORKDIR - рабочая папка
- ENV - настройка Python
- COPY - копирование файлов
- RUN - установка зависимостей
- CMD - запуск main.py

## Исключения .dockerignore:
- .venv/
- venv/
- .env
- .env.*
- .git/
- __pycache__/
- *.pyc
- *.log
- chat_history.txt
- *.pem
- *.key

## Команда сборки:
sudo docker build -t my-ai-agent:1.0 .


## Результат:
Docker-образ my-ai-agent:1.0 успешно собран.
