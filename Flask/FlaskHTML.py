from flask import Flask,render_template

app = Flask(__name__) # obj

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=80,host="0.0.0.0")