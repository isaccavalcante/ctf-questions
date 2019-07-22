 # -*- coding: utf-8 -*- 
from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
from flask import make_response
import writer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    cpf = db.Column(db.String(120))
    password = db.Column(db.String(80))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/invoice.php")
def get_invoice():
    seq = request.args.get("seq")
    user = db.session.query(User).get(seq)
    filename = writer.generate_invoice(user.name, user.cpf)
    with open(filename, "rb") as f:
        binary_pdf = f.read()
    response = make_response(binary_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        f'inline; filename={filename}'
    return response

@app.route("/invoice.php?name=<name>&seq=<seq>&cpf=<cpf>".replace("%", "a"))
def invoice(name, cpf, seq):
    print("------->", seq)
    user = db.session.query(User).get(seq)
    filename = writer.generate_invoice(user.name, user.cpf)
    with open(filename, "rb") as f:
        binary_pdf = f.read()
    response = make_response(binary_pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = \
        f'inline; filename={filename}'
    return response

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        cpf = request.form['cpf']
        password = request.form['password']

        user = User(name=name, cpf=cpf, password=password)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("invoice", name=name, cpf=cpf, seq=user.seq))
    return render_template("register.html")

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8080, host="0.0.0.0")