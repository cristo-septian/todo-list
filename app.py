from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)  

DB_NAME = "todo.db"


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_NAME):
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tugas TEXT NOT NULL,
                kategori TEXT CHECK(kategori IN ('Pribadi', 'Umum')) NOT NULL,
                tanggal_dibuat TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                tanggal_selesai TEXT DEFAULT NULL
            );
        ''')
        conn.commit()
        conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    if request.method == "POST":
        tugas = request.form["tugas"].strip()
        kategori = request.form["kategori"]
        if tugas and kategori in ("Pribadi", "Umum"):
            conn.execute(
                'INSERT INTO todo (tugas, kategori) VALUES (?, ?)',
                (tugas, kategori)
            )
            conn.commit()
        return redirect("/")

    todos = conn.execute('SELECT * FROM todo').fetchall()
    conn.close()
    return render_template("index.html", todos=todos)



@app.route("/selesai/<int:todo_id>")
def selesai(todo_id):
    selesai_waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = get_db_connection()
    conn.execute('UPDATE todo SET tanggal_selesai = ? WHERE id = ?', (selesai_waktu, todo_id))
    conn.commit()
    conn.close()
    return redirect("/")@app.route("/hapus/<int:todo_id>")
def hapus(todo_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM todo WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/hapus/<int:todo_id>")
def hapus(todo_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM todo WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5013)

