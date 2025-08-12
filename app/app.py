from flask import Flask
import psycopg2
import time
import sys

app = Flask(__name__)

def wait_for_database():
    """Wait for the database to be ready before starting the application"""
    max_retries = 30  # Maximum number of attempts
    retry_interval = 2  # Seconds to wait between attempts
    
    for attempt in range(max_retries):
        try:
            conn = psycopg2.connect(
                host='db', 
                dbname='students', 
                user='admin', 
                password='admin123',
                connect_timeout=5
            )
            conn.close()
            print("✅ Database connection successful!")
            return True
        except psycopg2.OperationalError as e:
            print(f"⏳ Database not ready (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:  # Don't sleep on the last attempt
                time.sleep(retry_interval)
    
    print("❌ Failed to connect to database after maximum retries")
    sys.exit(1)

@app.route('/')
def students():
    try:
        conn = psycopg2.connect(
            host='db', dbname='students', user='admin', password='admin123'
        )
        cur = conn.cursor()
        cur.execute("SELECT name FROM student")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return '<br>'.join(name for (name,) in rows)
    except Exception as e:
        return f"Database error: {str(e)}", 500

if __name__ == '__main__':
    print("🚀 Starting application...")
    wait_for_database()
    print("🌐 Starting Flask server...")
    app.run(host='0.0.0.0', debug=True)
