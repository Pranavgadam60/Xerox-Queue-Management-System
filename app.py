from flask import Flask, request, jsonify, render_template, send_file
import sqlite3
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():

    files = request.files.getlist('files[]')

    conn = sqlite3.connect("queue.db")
    cursor = conn.cursor()

    for file in files:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        cursor.execute(
            "INSERT INTO documents(filename) VALUES (?)",
            (file.filename,)
        )

    conn.commit()
    conn.close()

    return "Files uploaded successfully"

@app.route('/admin/files')
def admin_files():
    return jsonify(os.listdir("uploads"))

@app.route('/admin')
def admin():
    return send_file('admin.html')
if __name__ == '__main__':
    app.run(debug=True)