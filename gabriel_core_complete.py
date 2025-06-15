from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/core/ping", methods=["GET"])
def ping():
    return jsonify({"message": "Gabriel Core OK", "status": 200})

@app.route("/core/diagnostics", methods=["GET"])
def diagnostics():
    return jsonify({
        "gabriel": "running",
        "aiin_interface": "waiting",
        "loop_status": "active"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
