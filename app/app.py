from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def students():
    conn = psycopg2.connect(
        host='db', dbname='students', user='admin', password='admin123'
    )
    cur = conn.cursor()
    cur.execute("SELECT name FROM student")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return '<br>'.join(name for (name,) in rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

