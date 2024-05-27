from flask import Flask,render_template,request,session,redirect,send_file,url_for
from contact.contact import *
from flask_session import Session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    session["contact"] = Contacts("")
    return render_template('upload.html',columns = session["contact"].columns)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
    return "File type not allowed"


@app.route("/number",methods=['GET', 'POST'])
def number():
    session["contact"].num_index_label =[[int(request.form.get(f'num_index-{i}',-1)), request.form.get(f'num_label-{i}',"")] for i in range(session.get("no_of_number",2))]  
    print(session["contact"].num_index_label)
    print(session["contact"].get_num_index_labels())
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

@app.route('/download')
def download_file():
    file_path = 'Export.vcf'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
    
