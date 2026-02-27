from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

DATABASE = 'data.db'


def get_db_connection():
    """Create a database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/search', methods=['GET'])
def search():
    """
    Search endpoint - VULNERABLE to SQL injection
    This is intentionally insecure for demonstration purposes
    """
    code = request.args.get('code', '')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # VULNERABLE QUERY - directly interpolating user input
        # This allows SQL injection attacks
        query = f"SELECT * FROM data WHERE data = '{code}'"
        print(f"Executing query: {query}")  # For debugging

        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()

        if results:
            # Convert results to list of dicts
            data_list = [dict(row) for row in results]
            return jsonify({
                'success': True,
                'message': 'Access Granted! WiFi Password: Demo@2024',
                'results': data_list
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Invalid Code. Access Denied.',
                'results': []
            })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Database error: {str(e)}',
            'results': []
        }), 500


@app.route('/', methods=['GET'])
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'SQL Injection Demo API',
        'endpoints': {
            '/search?code=<code>': 'Search for a code (vulnerable to SQL injection)'
        }
    })


if __name__ == '__main__':
    # Check if database exists
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM data")
        count = cursor.fetchone()[0]
        print(f"Database connected. {count} records found.")
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")

    print("\n" + "="*50)
    print("SQL Injection Demo Server")
    print("="*50)
    print("Server running on http://127.0.0.1:5000")
    print("\nValid codes in database:")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data LIMIT 5")
    for row in cursor.fetchall():
        print(f"  - {row['data']}")
    conn.close()
    print("\nTry SQL injection payloads like:")
    print("  - ' OR '1'='1")
    print("  - ' OR 1=1 --")
    print("  - ' UNION SELECT data FROM data --")
    print("="*50 + "\n")

    app.run(debug=True, host='127.0.0.1', port=5000)
