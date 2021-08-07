from flask import Flask, render_template, request
import csv
import pandas as pd

app = Flask(__name__)


def CreateNewFile():
    fieldnames = ['Name', "last_name", "Age"]
    with open("details.csv", 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

def AppendFile(dct):
    fieldnames = ['Name', "last_name", "Age"]
    with open("details.csv", 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(dct)


new_file = CreateNewFile()


@app.route("/", methods=["POST", "GET"])
def details():
    if request.method == "POST":
        user_name = request.form["name"]
        user_last_name = request.form["sur-name"]
        user_age = request.form["age"]
        dct =[{'Name': user_name, "last_name":user_last_name, "Age": user_age}]
        AppendFile(dct)

        return render_template("forms.html")
    else:
        return render_template("index.html")


@app.route("/forms")
def forms():
    return render_template("forms.html")


if __name__ == "__main__":
    app.run(debug=True)