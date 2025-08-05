from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()
    expression = data.get("expression")
    if not expression:
        return jsonify({"error": "Missing 'expression'"}), 400

    result = subprocess.run(["./marina", expression], capture_output=True, text=True)
    return jsonify({"result": result.stdout.strip()})

if __name__ == "__main__":
    app.run(port=5000)
