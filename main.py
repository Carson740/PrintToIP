# main.py

from flask import Flask, render_template, request, redirect, url_for
import subprocess
import requests
import os

def printTo(printType, printerIP):
    subprocess.run(['python', 'printTo.py', printType, printerIP])

def checkValid(printType, printerIP):
    url = "http://" + printerIP
    try:
        r = requests.get(url)

        if any(x in r.text for x in labelPrinters) and printType in genericList:
            isValid = "WrongType"
        elif any(x in r.text for x in genericPrinters) and printType in labelList:
            isValid = "WrongType"
        else:
            isValid = True
        return isValid
    except Exception:
        isValid = "NoConnect"
        print(Exception)
        return isValid
    

labelList = ["print_label_4x6"]
labelPrinters = ["ZD621", "Printronix"]

genericList = ["print_pdf_b&w", "print_pdf_color"]
genericPrinters = ["Kyocera", "Ricoh"]

valid = False

TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./templates/static')

print(TEMPLATE_DIR)
print(STATIC_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

...

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    printer_ip = ''
    error_message = request.args.get('error_message')  # Get the error_message from the query parameters
    if request.method == 'POST':
        printer_ip = request.form['printer_ip']
        if 'print_pdf_b&w' in request.form:
            isValid = checkValid('print_pdf_b&w', printer_ip)
            if isValid == True:
                printTo('print_pdf_b&w', printer_ip)
            elif isValid == "WrongType":
                error = "Error: The specified printer is invalid for this print type."
            elif isValid == "NoConnect":
                error = "Error: Could not connect to printer"
            else:
                error = None
            return redirect(url_for('home', error_message=error, printer_ip=printer_ip))
        elif 'print_pdf_color' in request.form:
            isValid = checkValid('print_pdf_color', printer_ip)
            if isValid == True:
                printTo('print_pdf_color', printer_ip)
            elif isValid == "WrongType":
                error = "Error: The specified printer is invalid for this print type."
            elif isValid == "NoConnect":
                error = "Error: Could not connect to printer"
            else:
                error = None
            return redirect(url_for('home', error_message=error, printer_ip=printer_ip))
        elif 'print_label_4x6' in request.form:
            isValid = checkValid('print_label_4x6', printer_ip)
            if isValid == True:
                printTo('print_label_4x6', printer_ip)
            elif isValid == "WrongType":
                error = "Error: The specified printer is invalid for this print type."
            elif isValid == "NoConnect":
                error = "Error: Could not connect to printer"
            else:
                error = None
            return redirect(url_for('home', error_message=error, printer_ip=printer_ip))
    else:
        if 'printer_ip' in request.args:
            printer_ip = request.args['printer_ip']
    return render_template('home.html', error_message=error_message, printer_ip=printer_ip)  # Pass the error_message to the template

if __name__ == '__main__':
    app.run(debug=True)
