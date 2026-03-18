import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("study.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS study_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            hours REAL NOT NULL,
            completed INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = get_db_connection()
    records = conn.execute("SELECT * FROM study_records").fetchall()
    conn.close()

    total_records = len(records)
    completed_count = 0
    total_hours = 0

    for record in records:
        if record["completed"]:
            completed_count += 1
            total_hours += record["hours"]

    pending_count = total_records - completed_count

    return render_template(
        "index.html",
        records=records,
        total_records=total_records,
        completed_count=completed_count,
        pending_count=pending_count,
        total_hours=total_hours
    )


@app.route("/add", methods=["POST"])
def add_record():
    subject = request.form["subject"]
    hours = request.form["hours"]

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO study_records (subject, hours, completed) VALUES (?, ?, ?)",
        (subject, hours, 0)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("home"))


@app.route("/delete/<int:id>", methods=["POST"])
def delete_record(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM study_records WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("home"))


@app.route("/toggle/<int:id>", methods=["POST"])
def toggle_complete(id):
    conn = get_db_connection()

    record = conn.execute(
        "SELECT completed FROM study_records WHERE id = ?",
        (id,)
    ).fetchone()

    if record is not None:
        new_value = 0 if record["completed"] else 1

        conn.execute(
            "UPDATE study_records SET completed = ? WHERE id = ?",
            (new_value, id)
        )

        conn.commit()

    conn.close()
    return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)