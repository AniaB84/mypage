from flask import Flask
app = Flask(__name__)
from flask import render_template
from flask import request, redirect

@app.route('/me')
def me():
    return render_template("me.html")

@app.route('/contact/message', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
       items = ["email: ania@wp.pl" , "telefon: 888 999 000"]
       return render_template("contact.html", items=items)
    if request.method == 'POST':
       print("We received POST")
       print(request.form)
       

