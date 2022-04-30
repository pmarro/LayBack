from datetime import datetime
from sqlalchemy import ForeignKey

from app.extensions.database import CRUDMixin, db



class Designguide(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    #designguide_elements = db.relationship('DesignguideElement', backref = 'designguide', lazy = True)
    user = db.relationship('User', backref = 'designguide', uselist = False, lazy = True)
    logo = db.relationship('Logo', backref = 'designguide', uselist = False, lazy = True)
    font = db.relationship('Font', backref = 'designguide', uselist = False, lazy = True)
    color = db.relationship('Color', backref = 'designguide', uselist = False, lazy = True)
    keyword = db.relationship('Keyword', backref = 'designguide', uselist = False, lazy = True)


