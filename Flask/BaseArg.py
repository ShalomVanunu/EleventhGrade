from flask import Flask

app = Flask(__name__) # obj

@app.route("/")
def index():
    return "<h1>My First WEBPAGE</h1>"

@app.route("/ip/<ip>")
def get_class(ip):
    return f"<h2> your IP is {ip}</h2>"

if __name__ == "__main__":
    app.run(debug=True,port=80,host="0.0.0.0")