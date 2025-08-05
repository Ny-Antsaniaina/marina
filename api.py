from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()
    expression = data.get("expression")

    if not expression:
        return jsonify({"error": "Missing 'expression'"}), 400

    
    if not os.path.exists("./marina"):
        return jsonify({"error": "Marina binary not found"}), 500

    try:
        result = subprocess.run(["./marina", expression], capture_output=True, text=True, timeout=5)

        if result.returncode != 0:
            return jsonify({"error": "Marina failed", "details": result.stderr}), 500

        return jsonify({"result": result.stdout.strip()})

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Marina timed out"}), 504
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
