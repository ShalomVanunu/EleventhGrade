from flask import Flask,render_template

app = Flask(__name__) # obj

@app.route("/")
def basketball():

    return render_template("basketball.html", rishonscore= "88:70",telavivscore="99:80" )

if __name__ == "__main__":
    app.run(debug=True,port=80,host="0.0.0.0")