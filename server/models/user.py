from . import db
from werkzeug.security import generate_password_hash, check_password_hash
class User (db.Model):
    __tablename__ = 'users'

    id=db.Column(db.Integer, primary_key = True)
    username= db.Column(db.String(80), unique= True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
       self.password_hash = generate_password_hash(password)

    def check_password(self,password):
       self.check_password = check_password_hash(password)

    def __repr__(self):
      return f"<User id={self.id} username={self.username} email={self.email}>"