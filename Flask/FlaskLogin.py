from flask import Flask,render_template,request

app = Flask(__name__) # obj

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "shalom" and password == "Password1":
            return "<h1> You Hacked the site</h1>"
        else:
            return render_template("post.html")
    else:
        return render_template("post.html")



if __name__ == "__main__":
    app.run(debug=True,port=80,host="0.0.0.0")