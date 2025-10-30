from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

workers = [
    {"url": "http://worker1:5000", "load": 0},
    {"url": "http://worker2:5000", "load": 0}
]

@app.route("/job", methods=["POST"])
def assign_job():
    job = request.json
    chosen = min(workers, key=lambda w: w["load"])
    chosen["load"] += 1
    requests.post(f"{chosen['url']}/run", json=job)
    return jsonify({"assigned_to": chosen["url"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
