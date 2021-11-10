from flask import Flask,render_template,url_for,redirect

app = Flask(__name__) # obj

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ip/<ip>")
def get_ip(ip):
    return f"your IP is {ip}"

@app.route("/getip")
def get():
    return redirect(url_for("get_ip",ip="127.0.0.1"))


if __name__ == "__main__":
    app.run(debug=True,port=80,host="0.0.0.0")