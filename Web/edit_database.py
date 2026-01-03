import sqlite3
from werkzeug.security import generate_password_hash

connect = sqlite3.connect("sqlite.db", check_same_thread=False)
cursor = connect.cursor()

cursor.execute(
    "INSERT INTO user (id, username, password_hash) VALUES (?, ?, ?)",
    (1, "Admin", generate_password_hash("password123"))
)

connect.commit()

# Проверяем что добавилось
cursor.execute("SELECT * FROM user")
rows = cursor.fetchall()
print("Пользователи в БД:")
for row in rows:
    print(row)

connect.close()
