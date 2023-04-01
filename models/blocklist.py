from db import db

class Blocklist(db.Model):
    
    __tablename__ = "Blocklist"

    id = db.Column(db.Integer, primary_key=True)
    blocked_jti = db.Column(db.String(200), unique=True, nullable=False)

    