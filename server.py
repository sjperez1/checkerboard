from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def eight_by_eight():
    return render_template("index.html")

@app.route("/<int:num>")
def eight_by_four(num):
    return render_template("eightbyfour.html", num = num)

@app.route("/<int:x>/<int:y>")
def x_by_y(x, y):
    return render_template("xbyy.html", num1= x, num2=y)

if __name__ == "__main__":
    app.run(debug = True)