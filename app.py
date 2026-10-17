from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database for student records and academic marks
students = [
    {"id": 1, "name": "Alice Smith", "course": "Computer Science", "gpa": 3.8},
    {"id": 2, "name": "Bob Jones", "course": "DevOps Engineering", "gpa": 3.6}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Enterprise Student Record & Academic Management Platform"})

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = {
        "id": len(students) + 1,
        "name": data.get("name"),
        "course": data.get("course"),
        "gpa": data.get("gpa", 0.0)
    }
    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
