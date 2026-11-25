# Установка Docker
Для установки Docker использовались следующие команды:
Обновление списка пакетов:
sudo apt update

Установка необходимых инструментов:
sudo apt install -y ca-certificates curl

Добавление официального репозитория Docker и его ключа
Установка Docker:
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

Результат установки:
Docker Engine установлен успешно

Версия Docker: 29.10.0.
Версия Docker Compose: v5.0.0.

Проверка выполнялась командами:
docker --version
docker compose version

После установки удалось запустить Docker и проверить его работу на тестовом контейнере hello-world

Ошибки при установке:

Сначала возникали проблемы с системным временем Ubuntu. Из-за отключённой синхронизации появлялась ошибка Release file is not valid yet

Также временно не удавалось подключиться к download.docker.com (Connection refused)

Что удалось исправить:

Включена синхронизация системного времени. После восстановления доступа к репозиторию Docker удалось установить необходимые компоненты