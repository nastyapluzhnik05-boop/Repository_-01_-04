from dotenv import dotenv_values, find_dotenv
import os
import hashlib

path = find_dotenv()

if not path:
    print("Файл .env не найден")
    raise SystemExit(1)

file_key = dotenv_values(path).get("GIGACHAT_CREDENTIALS", "") or ""
loaded_key = os.getenv("GIGACHAT_CREDENTIALS", "") or ""

print("Файл настроек:", path)
print("Ключ в файле:", len(file_key), "символов")
print("Ключ после загрузки:", len(loaded_key), "символов")
print("Файл и загруженный ключ совпадают:", file_key == loaded_key)
print("Контрольная сумма из файла:",
      hashlib.sha256(file_key.encode()).hexdigest()[:16])
print("Контрольная сумма загруженного:",
      hashlib.sha256(loaded_key.encode()).hexdigest()[:16])
print("Scope в файле:", dotenv_values(path).get("GIGACHAT_SCOPE"))
print("Scope в окружении:", os.getenv("GIGACHAT_SCOPE"))
