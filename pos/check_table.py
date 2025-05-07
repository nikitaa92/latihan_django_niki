import sqlite3

# Sambungkan ke database SQLite
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Periksa apakah tabel pos_app_tableresto ada
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pos_app_tableresto';")
table_exists = cursor.fetchone()

if table_exists:
    print("Tabel 'pos_app_tableresto' ada!")
else:
    print("Tabel 'pos_app_tableresto' tidak ada!")

# Tutup koneksi
conn.close()