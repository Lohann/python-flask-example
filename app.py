from flask import Flask, Response
import os

app = Flask(__name__)
port = os.environ.get("APP_PORT")
print(port)
count = 0

@app.route('/health')
def health():
    return Response('ok', status=200)

@app.route("/")
def hello_world():
    return "ola mundo"

@app.route("/counter")
def counter():
    global count
    count += 1
    return str(count)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
