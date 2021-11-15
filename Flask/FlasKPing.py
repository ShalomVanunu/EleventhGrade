from flask import Flask,render_template,request
import subprocess
app = Flask(__name__) # obj

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        ip = request.form.get("ping")
        ping = subprocess.Popen(f"ping {ip}")
        return f"<h1>{ping}</h1>"
    else:
        return render_template("ping.html")



if __name__ == "__main__":
    app.run(debug=True,port=80,host="0.0.0.0")