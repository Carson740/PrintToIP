from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    printer_ip = ''
    if request.method == 'POST':
        printer_ip = request.form['printer_ip']
        # Run the script with the specified printer IP address
        subprocess.run(['python', 'printTo.py', printer_ip])
        return redirect(url_for('home', printer_ip=printer_ip))
    else:
        if 'printer_ip' in request.args:
            printer_ip = request.args['printer_ip']
    return render_template('home.html', printer_ip=printer_ip)

if __name__ == '__main__':
    app.run(debug=True)
