import sqlite3

connection = sqlite3.connect(
    "ir_system.db",
    check_same_thread=False
)

cursor = connection.cursor()

cursor.execute('''

CREATE TABLE IF NOT EXISTS search_logs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    query TEXT

)

''')

connection.commit()