from flask import Flask

app = Flask(__name__) # obj

@app.route("/")
def index():
    return "<h1>My First WEBPAGE</h1>"

@app.route("/class")
def get_class():
    return "<h2> wellcome to Class</h2>"

if __name__ == "__main__":
    app.run(debug=True,port=80,host="0.0.0.0")