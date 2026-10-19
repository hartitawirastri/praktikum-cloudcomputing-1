import sqlite3
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Fungsi inisialisasi database SQLite
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            deskripsi TEXT NOT NULL
        )
    ''')
    cursor.execute('SELECT COUNT(*) FROM items')
    if cursor.fetchone()[0] == 0:
        cursor.execute('INSERT INTO items (nama, deskripsi) VALUES (?, ?)', 
                       ('Modul Cloud Computing', 'Integrasi Flask dengan Database SQLite & Docker Jenkins'))
        cursor.execute('INSERT INTO items (nama, deskripsi) VALUES (?, ?)', 
                       ('Tugas Praktikum', 'Berhasil terhubung ke database SQLite!'))
        conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    conn.close()
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Praktikum Cloud Computing - Database Test</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f6f9; }
            .card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 600px; margin: 0 auto; }
            h1 { color: #2c3e50; font-size: 22px; }
            .badge { background-color: #27ae60; color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold; font-size: 14px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
            th { background-color: #3498db; color: white; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1> Praktikum Cloud Computing Modul 2</h1>
            <p>Status Database: <span class="badge">CONNECTED (SQLite DB)</span></p>
            <h3>Data dari Database:</h3>
            <table>
                <tr><th>ID</th><th>Nama</th><th>Deskripsi</th></tr>
                {% for item in items %}
                <tr><td>{{ item[0] }}</td><td>{{ item[1] }}</td><td>{{ item[2] }}</td></tr>
                {% endfor %}
            </table>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, items=items)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
