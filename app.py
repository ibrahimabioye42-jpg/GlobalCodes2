# from flask import Flask, jsonify

# app = Flask(__name__)

# data = {
#     "name": "john doe",
#     "age": "30",
#     "city":"New York"
# }

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)
    
from flask import Flask, jsonify

app = Flask(__name__)
Student = [
    {'id': 1, 'name': 'Mr. Money', 'age': 30, 'city': 'New York'},
    {'id': 2, 'name': 'CashMoney', 'age': 25, 'city': 'Los Angeles'},
    {'id': 3, 'name': 'mike johnson', 'age': 35, 'city': 'Chicago'}
]

@app.route('/api/data/', methods=['GET'])
def get_data():
    return jsonify(Student)

@app.route('/api/students/<int:id>', methods=['GET'])
def get_student(id):
    for i in Student:
        if i['id'] == id:
            return jsonify(i)
        return jsonify({'message': "student not found"})

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/api/students', methods=['POST'])
def create_student():
    new_student = {
        'id': 6,
        'name':'Mr.Cashmoney',
        'age':30,
        'city': 'New York'
    }
    Student.append(new_student)
    return jsonify(new_student), 201
    