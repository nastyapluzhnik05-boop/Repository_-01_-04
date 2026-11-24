# Установка инструментов
Команды установки Git: sudo apt install git
Команды установки Python и venv: sudo apt install -y python3 python3-pip python3-venv
Команда установки зависимостей: python -m pip install -r requirements.txt
Результат pip check: 
python -m pip list
python -m pip check
Ошибок и конфликтов быть не должно
Ошибки и их причины: не выданы права sudo, файл requirements.txt не читался
Что удалось исправить: добавила sudo перед apt, перешла в нужную папку проекта, чтобы файл requirements.txt, который находится в этой папке корректно читался
