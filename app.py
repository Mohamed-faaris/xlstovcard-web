from flask import Flask,render_template,request
from contact.contact import *

contacts = Contacts(" ")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('name.html',columns = contacts.columns)

@app.route("/name",methods=['GET', 'POST'])
def name():
    if request.method != "POST":
        return render_template('name.html',columns = contacts.columns)
        

@app.route("/number",methods=['GET', 'POST'])
def number():
    if request.method != "POST":
        return render_template('number.html',columns = contacts.columns,no_of_number = 2)
    try:
        no_of_number = int(request.form["no_of_number"])
    except:
        no_of_number = 2
    return render_template('number.html',columns = contacts.columns,no_of_number = no_of_number)
    

@app.route("/email",methods=['GET', 'POST'])
def email():
    if request.method != "POST":
        return render_template('email.html',columns = contacts.columns)
    

@app.route("/groups",methods=['GET', 'POST'])
def groups():
    if request.method != "POST":
        return render_template('groups.html',columns = contacts.columns)
    
@app.route("/addional",methods=['GET', 'POST'])
def addional():
    if request.method != "POST":
        return render_template('addional.html',columns = contacts.columns)
    

if __name__ == '__main__':
    app.run(debug=True)
