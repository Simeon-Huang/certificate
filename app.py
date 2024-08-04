from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# 连接数据库
def get_db_connection():
    conn = sqlite3.connect('certificates.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM certificates
        WHERE 
            name LIKE ? OR
            moe_position LIKE ? OR
            certification_program LIKE ? OR
            certification_standard LIKE ? OR
            certification_date LIKE ? OR
            certificate_number LIKE ?
    ''', (f'%{query}%',) * 6)
    results = cur.fetchall()
    conn.close()

    certificates = []
    for row in results:
        certificates.append({
            "name": row["name"],
            "moe_position": row["moe_position"],
            "certification_program": row["certification_program"],
            "certification_standard": row["certification_standard"],
            "certification_date": row["certification_date"],
            "certificate_number": row["certificate_number"]
        })

    return jsonify(certificates)

if __name__ == '__main__':
    app.run(debug=True)
