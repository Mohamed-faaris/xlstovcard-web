from flask import Flask,render_template,request,session,redirect
from contact.contact import *
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    session["contact"] = Contacts("")
    return render_template('name.html',columns = session["contact"].columns)

@app.route("/number",methods=['GET', 'POST'])
def number():
    session["contact"].num_index_label =[ [request.form.get(f'num_label-{i}',""),int(request.form.get(f'num_index-{i}',-1))] for i in range(session.get("no_of_number",2))]  
    print(session["contact"].num_index_label)
    if request.method == "POST":
        return render_template('number.html',columns = session["contact"].columns,no_of_number = session.get("no_of_number",2),phone = session["contact"].num_index_label)
    return render_template('number.html',columns = session["contact"].columns,no_of_number = session.get("no_of_number",2),phone = session["contact"].num_index_label)

@app.route("/no_of_number",methods=['GET', 'POST'])
def num_number():
    try:
        session["no_of_number"] = int(request.form["no_of_number"])
    except:
        pass
    return redirect("/number")

@app.route("/email",methods=['GET', 'POST'])
def email():
    if request.method == "POST":
        return render_template('email.html',columns = session["contact"].columns,no_of_email = session.get("no_of_email",2))
    return render_template('email.html',columns = session["contact"].columns,no_of_email = session.get("no_of_email",2))

@app.route("/no_of_email",methods=['GET', 'POST'])
def num_email():
    try:
        session["no_of_email"] = int(request.form["no_of_email"])
    except:
        pass
    return redirect("/email")

@app.route("/groups",methods=['GET', 'POST'])
def groups():
    if request.method != "POST":
        return render_template('groups.html',columns = session["contact"].columns)
    
@app.route("/addional",methods=['GET', 'POST'])
def addional():
    if request.method != "POST":
        return render_template('addional.html',columns = session["contact"].columns)
    

if __name__ == '__main__':
    app.run(debug=True)
    
