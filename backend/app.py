from flask import Flask, jsonify
import os, psycopg2

app = Flask(__name__)
def get_db_connection():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        dbname=os.environ['DB_NAME']
    )

@app.route('/bulletins')
def bulletins():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, message, created_at FROM bulletins ORDER BY created_at DESC;')
    rows = cur.fetchall()
    cur.close(); conn.close()
    return jsonify([
        {'id': r[0], 'message': r[1], 'created_at': r[2].isoformat()}
        for r in rows
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
