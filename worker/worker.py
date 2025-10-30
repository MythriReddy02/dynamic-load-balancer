from flask import Flask, request
import time

app = Flask(__name__)

@app.route("/run", methods=["POST"])
def run_job():
    job = request.json
    print(f"Running job: {job}")
    time.sleep(3)
    print(f"Completed job: {job}")
    return "done"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
