Як користуватися програмою
Запуск програми: python3 main.py

Додавання контакту:
python3 main.py contact add "John Doe" "123 Elm St" "+1234567890" "john.doe@example.com" "1990-12-01"

Пошук контактів:
python3 main.py contact search "John"

Редагування контакту:
python3 main.py contact edit 0 --name "Jane Doe" --phone "+0987654321"

Видалення контакту:
python3 main.py contact delete 0

Перегляд контактів з днями народження через 30 днів:
python3 main.py contact list 30

Додавання нотатки:
python3 main.py note add "Meeting Notes" "Discuss project roadmap."

Пошук нотаток:
python3 main.py note search "Meeting"

Редагування нотатки:
python3 main.py note edit 0 --title "Updated Meeting Notes" --content "Updated content."

Видалення нотатки:
python3 main.py note delete 0