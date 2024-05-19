from flask import Flask,render_template,request,session,redirect
from contact.contact import *
from flask_session import Session

contacts = Contacts(" ")
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    return render_template('name.html',columns = contacts.columns)

@app.route("/number",methods=['GET', 'POST'])
def number():
    print(request.form)
    if request.method == "POST":
        return render_template('number.html',columns = contacts.columns,no_of_number = session.get("no_of_number",2))
    return render_template('number.html',columns = contacts.columns,no_of_number = session.get("no_of_number",2))

@app.route("/no_of_number",methods=['GET', 'POST'])
def num_number():
    try:
        session["no_of_number"] = int(request.form["no_of_number"])
        #no_of_number = int(request.args.get('no_of_number'))
    except:
        pass
    return redirect("/number")

@app.route("/email",methods=['GET', 'POST'])
def email():
    phone_index_labels =[[0,0] for _ in session.get("no_of_email",2)] 
    print(phone_index_labels)
    if request.method == "POST":
        return render_template('email.html',columns = contacts.columns,no_of_email = session.get("no_of_email",2))
    return render_template('email.html',columns = contacts.columns,no_of_email = session.get("no_of_email",2),phone = phone_index_labels)

@app.route("/no_of_email",methods=['GET', 'POST'])
def num_email():
    try:
        session["no_of_email"] = int(request.form["no_of_email"])
        #no_of_email = int(request.args.get('no_of_email'))
    except:
        pass
    return redirect("/email")

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
