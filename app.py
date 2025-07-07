from flask import Flask

app = Flask(__name__)

@app.route("/")
def initial():
    return "Hello world!!!"
    

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)