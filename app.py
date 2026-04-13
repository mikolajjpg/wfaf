from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = "todo.db"
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
done INTEGER NOT NULL DEFAULT 0 CHECK (done IN (0,1)),
created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_tasks_done ON tasks(done);
CREATE INDEX IF NOT EXISTS idx_tasks_created_at ON tasks(created_at);
"""

def get_db():
    if "db" not in g:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foregin_keys=ON;")
        g.db = conn

    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.executescript(SCHEMA_SQL)
    db.commit()

@app.cli.command("init-db")
def init_db_command():
    init_db()
    print("Zainicjowano baze danych")

@app.cli.command("seed-db")
def seed_db_command():
    db = get_db()
    howManyTasks = db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    if howManyTasks == 0:
        db.executemany("INSERT INTO tasks(title, done) VALUES (?,?)",[["Sniadanie",1],["Wyjsc po mleko",0],["zmywac naczynia", 0]])
        db.commit()

        print("Dane przykladowe zostaly dodane do tabeli tasks.")
    else:
        print("X Tabela tasks zawiera juz dane, seedowanie przerwane.")



@app.route("/ping_db")
def ping_db():
    db = get_db()
    db.execute("SELECT 1").fetchone()
    return render_template("ping.html")



@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":

    app.run(debug=True)