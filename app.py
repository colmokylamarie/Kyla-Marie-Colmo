from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory student "database"
students = [
    {"id": 1, "name": "Kyla Marie Colmo", "year": 3, "section": "Stallman"},
    {"id": 2, "name": "Jona Pagunsan", "year": 2, "section": "Torvalds"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = {
        "id": len(students) + 1,
        "name": data.get("name"),
        "year": data.get("year"),
        "section": data.get("section")
    }
    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(debug=True)
