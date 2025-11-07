from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API!"

@app.route('/student', methods=['GET'])
def get_student():
    student_info = {
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    }
    return jsonify(student_info)

if __name__ == '__main__':
    app.run(debug=True)
