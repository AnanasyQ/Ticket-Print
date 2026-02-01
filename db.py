# Робота локальної бази даних SQLite
import sqlite3

def init_db(conn):
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(""" CREATE TABLE IF NOT EXISTS cartridges(
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 archive INTEGER NOT NULL DEFAULT 0,
                 note TEXT);

                 CREATE TABLE IF NOT EXISTS history(
                 cartridge_id INTEGER NOT NULL,
                 date TEXT NOT NULL, -- ISO: YYYY-MM-DD
                 FOREIGN KEY(cartridge_id) REFERENCES cartridges(id)
                       ON UPDATE CASCADE ON DELETE CASCADE);

                 CREATE TABLE IF NOT EXISTS availability(
                 cartridge_id INTEGER NOT NULL,
                 stock INTEGER NOT NULL,
                 empty INTEGER NOT NULL,
                 used INTEGER NOT NULL,
                 FOREIGN KEY(cartridge_id) REFERENCES cartridges(id)
                       ON UPDATE CASCADE ON DELETE CASCADE);

                 CREATE TABLE IF NOT EXISTS statistics(
                 cartridge_id INTEGER NOT NULL,
                 month INTEGER NOT NULL, -- 1..12
                 count INTEGER NOT NULL,
                 FOREIGN KEY(cartridge_id) REFERENCES cartridges(id)
                       ON UPDATE CASCADE ON DELETE CASCADE);
                 """)
    conn.commit()
