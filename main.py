# Головний файл запуску
import sqlite3
import db

conn = sqlite3.connect('TicketPrint.db')
db.init_db(conn)
conn.close()