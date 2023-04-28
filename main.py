# main.py

from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def home():
    printer_ip = ''
    if request.method == 'POST':
        printer_ip = request.form['printer_ip']
        if 'print_pdf' in request.form:
            # Run the script with the specified printer IP address and command 'print_pdf'
            print(printer_ip, "print_pdf")
            subprocess.run(['python', 'printTo.py', 'print_pdf', printer_ip])
        elif 'print_4x6label' in request.form:
            # Run the script with the specified printer IP address and command 'print_text'
            print(printer_ip, "print_4x6label")
            subprocess.run(['python', 'printTo.py', 'print_4x6label', printer_ip])
        return redirect(url_for('home', printer_ip=printer_ip))
    else:
        if 'printer_ip' in request.args:
            printer_ip = request.args['printer_ip']
    return render_template('home.html', printer_ip=printer_ip)

if __name__ == '__main__':
    app.run(debug=True)
