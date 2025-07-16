from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector
import os

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST"),
        port=int(os.environ.get("MYSQL_PORT", 3306)),
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE")
    )
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        message = request.form["message"]
        cursor.execute("INSERT INTO message (content) VALUES (%s)", (message,))
        conn.commit()
        return redirect("/")

    cursor.execute("SELECT id,content FROM message")
    messages = cursor.fetchall()
    conn.close()

    return render_template("index.html", messages=messages)

@app.route("/api/messages")
def api_messages():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM message")
    messages = cursor.fetchall()
    conn.close()
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
