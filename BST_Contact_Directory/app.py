from flask import Flask, request, jsonify, render_template
from bst_backend import BSTContactDirectory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

directory = BSTContactDirectory()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add_contact():
    data = request.json
    if not data:
        return {"error": "No JSON data received"}, 400
    directory.insert(data['name'], data['phone'], data['email'])
    return jsonify({"message": "Contact added successfully!"})

@app.route('/search/<name>', methods=['GET'])
def search_contact(name):
    contact = directory.search(name)
    if contact:
        return jsonify({"name": contact.name, "phone": contact.phone, "email": contact.email})
    else:
        return jsonify({"error": "Contact not found"}), 404

@app.route('/delete/<name>', methods=['DELETE'])
def delete_contact(name):
    directory.delete(name)
    return jsonify({"message": f"Contact '{name}' deleted (if existed)"})

@app.route('/all', methods=['GET'])
def get_all():
    return jsonify(directory.display())

if __name__ == "__main__":
    app.run(debug=True)
