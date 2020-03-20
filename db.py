from flask import Flask, jsonify, request

app = Flask(__name__)

db = [
    {
        "student_id": ["1001"],
        "first_name": ["Sammy "],
        "last_name": ["Tee"],
        "dob(date of birth)": ["December 5th"],
        "amount_due": ["1 Million"]
    },
    {
        "student_id": ["1002"],
        "first_name": ["Kiran"],
        "last_name": ["G"],
        "dob(date of birth)": ["March 8th"],
        "amount_due": ["2 Million"]
    },
    {
        "student_id": ["1003"],
        "first_name": ["Sukhi"],
        "last_name": ["K"],
        "dob(date of birth)": ["January 19th"],
        "amount_due": ["3 Million"]
    }
]

@app.route('/db')
def hello():
    return jsonify(db)

#ADD
@app.route('/db', methods=['POST'])
def add_db():
    student = request.get_json()
    db.append(student)
    return {'id': len(db)}, 200

#UDATE
@app.route('/db/<int:index>', methods=['PUT'])
def update_db(index):
    student = request.get_json()
    db[index] = student
    return jsonify(db[index]), 200

#DELETE
@app.route('/db/<int:index>', methods=['DELETE'])
def delete_db(index):
    db.pop(index)
    return 'None', 200

app.run()