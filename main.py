from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def details():
    if request.method == "POST":
        user_name = request.form["name"]
        user_last_name = request.form["sur-name"]

        print(user_name, user_last_name)

        return render_template("forms.html")
    else:
        return render_template("index.html")


@app.route("/forms")
def forms():
    return render_template("forms.html")


if __name__ == "__main__":
    app.run(debug=True)