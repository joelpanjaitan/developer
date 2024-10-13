from flask import request, jsonify, Flask
from database_config import get_data_connection

indexFile = Flask(__name__)

@indexFile.route('/employees',methods=['POST'])
def create_employee():
    data = request.json()
    connection = get_data_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)
    ''', (data['name'], data['position'], data['salary']))
    connection.commit()
    employee_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return jsonify({'id': employee_id}), 201

@indexFile.route("/employees",methods=["GET"])
def get_all_employees():
    connection = get_data_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(employees)

@indexFile.route('/employees/<int:emp_id>',methods=["PUT"])
def update_employee_data(emp_id):
    data = request.json()
    connection = get_data_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE employees SET name=%s, position=%s, salary=%s WHERE id=%s
    ''', (data['name'], data['position'], data['salary'], emp_id))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'status': 'Employee updated'}), 200

@indexFile.route('/employees/<int:emp_id>',methods=['DELETE'])
def delete_employee_data(emp_id):
    connection = get_data_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM employees WHERE id=%s',(emp_id,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'status':"Employee deleted"}), 200

if __name__ == '__main__':
    indexFile.run(host="localhost",port=8000,debug=True)

