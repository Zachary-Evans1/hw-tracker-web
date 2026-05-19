from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "assignments.json"

def load_assignments():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_assignments(assignments):
    with open(DATA_FILE, "w") as f:
        json.dump(assignments, f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/assignments", methods=["GET"])
def get_assignments():
    return jsonify(load_assignments())

@app.route("/assignments", methods=["POST"])
def add_assignment():
    data = request.json
    assignments = load_assignments()
    assignments.append({
        "courseName": data["courseName"],
        "hwName": data["hwName"],
        "dueDate": data["dueDate"],
        "completed": False
    })
    save_assignments(assignments)
    return jsonify({"success": True})

@app.route("/assignments/<int:index>", methods=["DELETE"])
def remove_assignment(index):
    assignments = load_assignments()
    if 0 <= index < len(assignments):
        assignments.pop(index)
        save_assignments(assignments)
    return jsonify({"success": True})

@app.route("/assignments/<int:index>/complete", methods=["PUT"])
def mark_complete(index):
    assignments = load_assignments()
    if 0 <= index < len(assignments):
        assignments[index]["completed"] = True
        save_assignments(assignments)
    return jsonify({"success": True})

@app.route("/assignments/<int:index>/incomplete", methods=["PUT"])
def mark_incomplete(index):
    assignments = load_assignments()
    if 0 <= index < len(assignments):
        assignments[index]["completed"] = False
        save_assignments(assignments)
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)