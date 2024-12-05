from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Clanok(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meno = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    recenzia = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Clanok: {self.meno}'