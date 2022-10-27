from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "DEU CERTO mundo"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

# sudo apt install python3-pip
# pip3 install -r requirements.txt
