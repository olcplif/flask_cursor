from flask import Flask, render_template
from calc import Calc

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')


@app.route("/calc/<num1>/<num2>/<act>", methods=["GET"])
def calc_example(num1, num2, act):
    calc_str = Calc(num1, num2, act).show_calc()
    return render_template("example.html", calc_app=calc_str)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
