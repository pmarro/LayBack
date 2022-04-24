from sqlalchemy import ForeignKey
from app.extensions.database import db, CRUDMixin
from flask_login import UserMixin 

class User(db.Model, CRUDMixin, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100))
  company_email = db.Column(db.String(120), index = True, unique = True)
  password = db.Column(db.String(120))
  designguide_id = db.Column(db.Integer, db.ForeignKey('designguide.id'), nullable = True)
  