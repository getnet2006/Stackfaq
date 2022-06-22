from app import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(75), nullable=False)

    def __repr__(self) -> str:
        return f'<Questions {self.question}>'