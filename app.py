from flask import Flask,render_template
from contact.contact import *

contacts = Contacts(" ")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',columns = contacts.columns)

if __name__ == '__main__':
    app.run(debug=True)
