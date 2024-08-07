import numpy as np
from flask import Flask, render_template, request, session

from src.utils import plot_log

app = Flask(__name__)
app.secret_key = b"111_fx\1"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/index")
def back_to_index():
    return render_template("index.html")


@app.route("/authors")
def authors():
    return render_template("authors.html")


@app.route("/zagadnienie", methods=["POST", "GET"])
def zagadnienie():
    feedback = ""
    if request.method == "POST":
        try:
            if float(request.form["base"]) > 0 and float(request.form["base"]) != 1:
                session["base"] = float(request.form["base"])
                feedback = "Zmieniono podstawę logarytmu na " + request.form["base"] + "."
            else:
                session["base"] = np.e
                feedback = "Podstawa logarytmu musi być liczbą dodatnią nierówną 1. Ustawiono domyślną wartość e."
        except ValueError:
            session["base"] = np.e
            feedback = "Podstawa logarytmu musi być liczbą dodatnią nierówną 1. Ustawiono domyślną wartość e."
    base = session.get("base", np.e)
    return render_template(
        "zagadnienie.html", plot=plot_log(base=base, xmin=0.001, xmax=20.001), feedback=feedback
    )


if __name__ == "__main__":
    app.run(debug=True)
