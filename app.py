from flask import Flask,render_template,request,session,redirect,send_file,url_for
from contact.contact import *
from flask_session import Session
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
            
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def get_names(name:str):
    value = request.form.get(name,"")
    print(value)
    if value == "None":
        return None
    elif value == "":
        return ""
    elif value == "custom":
        value = request.form.get(name+"_text","")
        return [-1,value]
    return int(value)


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            # session["contact"] = Contacts('uploads/file.xlsx')
            # return redirect("/name")  
            return "No selected file"
        if file and allowed_file(file.filename):
            os.makedirs('uploads', exist_ok=True)
            file.save('uploads/file.xlsx')
            session["contact"] = Contacts('uploads/file.xlsx')
            session["filename"] = file.filename
            return redirect("/name")            
        else:
            return "Invalid file type"
    return render_template("upload.html")


@app.route("/name",methods=['POST','get'])
def name():
    if request.method == "POST":
        session["contact"].name_index = [get_names("prefix"),\
                                         get_names("first_name"),\
                                         get_names("middle_name"),\
                                         get_names("last_name"),\
                                         get_names("suffix")]
        print(request.form.items(),[get_names("prefix"),\
                                    get_names("first_name"),\
                                    get_names("middle_name"),\
                                    get_names("last_name"),\
                                    get_names("suffix")],    
                                    session["contact"].name_index)
    return render_template("name.html",columns=session["contact"].columns,name_index = session["contact"].name_index)


@app.route("/number",methods=['GET', 'POST'])
def number():
    print(session["contact"].num_index_labels,"|  |",request.form)
    if request.method == "POST":
        session["contact"].num_index_labels =[[int(request.form.get(f'num_index-{i}',-1)), request.form.get(f'num_label-{i}',"")] for i in range(session.get("no_of_number",2))]  
    return render_template('number.html',columns = session["contact"].columns,no_of_number = session.get("no_of_number",2),phone = session["contact"].num_index_labels)


@app.route("/no_of_number",methods=['GET', 'POST'])
def num_number():
    try:
        session["no_of_number"] = int(request.form["no_of_number"])
        while len(session["contact"].num_index_labels)< session["no_of_number"] :
            session["contact"].num_index_labels.append([-1,""])
    except:
        pass 
    return redirect("/number")


@app.route("/email",methods=['GET', 'POST'])
def email():
    if request.method == "POST":
        session["contact"].email_index_labels =[[int(request.form.get(f'email_index-{i}',-1)), request.form.get(f'email_label-{i}',"")] for i in range(session.get("no_of_email",2))]  
    return render_template('email.html',columns = session["contact"].columns,no_of_email = session.get("no_of_email",2),email = session["contact"].email_index_labels)


@app.route("/no_of_email",methods=['GET', 'POST'])
def email_email():
    try:
        session["no_of_email"] = int(request.form["no_of_email"])
        while len(session["contact"].email_index_labels)< session["no_of_email"] :
            session["contact"].email_index_labels.append([-1,""])
    except:
        pass 
    return redirect("/email")


@app.route("/group",methods=['GET', 'POST'])
def groups():
    if request.method == "POST":
        session["contact"].groups_index = [get_names(f"groups_name-{i}") for i in range(1,session.get("no_of_groups",2)+1)]
    print(session["contact"].groups_index,request.form,"|||",session.get("no_of_groups",2))
    return render_template("group.html",columns=session["contact"].columns,groups_index = session["contact"].groups_index, no_of_groups=session.get("no_of_groups",2))


@app.route("/no_of_groups",methods=['GET', 'POST'])
def no_of_group():
    session["no_of_groups"] = int(request.form.get("no_of_groups",2))
    while len(session["contact"].groups_index)< session["no_of_groups"] :
        print("hello")
        session["contact"].groups_index.append("")
    return redirect("/group")


@app.route("/addional",methods=['GET', 'POST'])
def addional():
    if request.method != "POST":
        return render_template('addional.html',columns = session["contact"].columns)


@app.route('/download')
def download_file():
    print("start")
    print(session['contact'].email_index_labels,session['contact'].groups_index,session['contact'].num_index_labels,session['contact'].name_index,sep=" || ")
    session['contact'].build()
    print("stop")
    file_path = 'Export.vcf'
    return send_file(file_path, as_attachment=True)


@app.route('/test')
def test():
    return render_template()



if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
    
