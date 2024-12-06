from flask import Flask
from flask import render_template
from forms import PridajClanokFormular
from models import Clanok, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///table.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.secret_key = "tvoj_krastny_sigma_klucik"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/pricing")
def pricing():
    return render_template('pricing.html')

@app.route('/contact', methods=["POST", "GET"])
def contact():
    f = PridajClanokFormular()
    if f.validate_on_submit():
        nc = Clanok(meno=f.meno.data, email=f.email.data, recenzia=f.recenzia.data)

        db.session.add(nc)
        db.session.commit()

        return render_template('contact.html', form=f, success=True)

    return render_template('contact.html', form=f, success=False)

@app.route("/members")
def members():
    members_list = Clanok.query.all()
    return render_template("members.html", members=members_list)


with app.app_context():
    db.create_all()