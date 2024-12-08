from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
import psycopg2

app = Flask(__name__)
CORS(app, origins=["https://evorxys.github.io"])  # Allow requests from your GitHub Pages domain

# Database connection string
DATABASE_URL = "postgresql://DATS_owner:U3VNAwsrH1uK@ep-dawn-queen-a1bp9gxj.ap-southeast-1.aws.neon.tech/DATS?sslmode=require"

def connect_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/insert', methods=['POST'])
def insert_data():
    try:
        data = request.json
        name = data['name']
        age = data['age']

        conn = connect_db()
        cursor = conn.cursor()

        # Insert into the table
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Data inserted successfully!"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Failed to insert data."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
