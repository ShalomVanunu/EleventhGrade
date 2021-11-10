from flask import Flask,redirect

app = Flask(__name__) # obj

@app.route("/")
def index():
    return "<h1>My First WEBPAGE</h1>"

@app.route("/ynet")
def get_class():
    return redirect("https://www.ynet.co.il")

if __name__ == "__main__":
    app.run(debug=True,port=80,host="0.0.0.0")