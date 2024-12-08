from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database connection string
DATABASE_URL = "postgresql://DATS_owner:U3VNAwsrH1uK@ep-dawn-queen-a1bp9gxj.ap-southeast-1.aws.neon.tech/DATS?sslmode=require"

def connect_db():
    """Establishes a connection to the PostgreSQL database."""
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@app.route('/insert', methods=['POST'])
def insert_data():
    """API endpoint to insert data into the users table."""
    try:
        data = request.json
        name = data['name']
        age = data['age']

        # Connect to the database
        conn = connect_db()
        cursor = conn.cursor()

        # Insert into the table
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()

        # Close database connections
        cursor.close()
        conn.close()

        return jsonify({"message": "Data inserted successfully!"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Failed to insert data.", "error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
