from flask import Flask, render_template, request
import csv
import pandas as pd
import win32print, win32api
import os
from get_path import get_path
path = get_path()


app = Flask(__name__)


def pdf_printer(pdf_name):
    path = os.getcwd()
    path = str(path.replace("\\", "\\\\"))

    GHOSTSCRIPT_PATH = path + "\\GHOSTSCRIPT\\bin\\gswin32.exe"
    GSPRINT_PATH = path + "\\\GSPRINT\\gsprint.exe"

    # YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
    currentprinter = win32print.GetDefaultPrinter()

    print_pdf = pdf_name

    win32api.ShellExecute(0, 'open', GSPRINT_PATH,
                          '-ghostscript "' + GHOSTSCRIPT_PATH + '" -printer "' + currentprinter + '" "+ print_pdf +"',
                          '.', 0)

def CreateNewFile():
    fieldnames = ['Name', "last_name", "Age"]
    with open("details.csv", 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

def AppendFile(dct):
    fieldnames = ['Name', "last_name", "Age"]
    with open("details.csv", 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerows(dct)


#new_file = CreateNewFile()


@app.route("/", methods=["POST", "GET"])
def details():
    if request.method == "POST":
        user_name = request.form["name"]
        user_last_name = request.form["sur-name"]
        user_age = request.form["age"]
        # printer_1 = request.form["printer_1"]
        # print(printer_1)
        dct =[{'Name': user_name, "last_name":user_last_name, "Age": user_age}]

        if os.path.exists(path.get_project_root() + "//details.csv"):
            AppendFile(dct)
            print("File exists")
        else:
            CreateNewFile()
            AppendFile(dct)
            print("No such file")

        if request.method == "GET":
            if request.form.get("printer_1"):
                print("its printer 1")

        return render_template("forms.html")
    else:
        return render_template("index.html")


@app.route("/forms", methods=["POST", "GET"])
def forms():
    if request.method == "POST":
        if request.form.get("printer_1"):
            pdf_printer("account-modification-form")

    return render_template("forms.html")


if __name__ == "__main__":
    app.run(debug=True)