from datetime import datetime
from sqlalchemy import ForeignKey

from app.extensions.database import CRUDMixin, db


class Designguide(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    designguide_elements = db.relationship('DesignguideElement', backref = 'designguide', lazy = True)
    user = db.relationship('User', backref = 'designguide', uselist = False, lazy = True)

class DesignguideElement(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    font_id = db.Column(db.Integer, db.ForeignKey('font.id'), nullable = True)
    design_guide_id = db.Column(db.Integer, db.ForeignKey('designguide.id'), nullable = True )
    keyword_id = db.Column(db.Integer, db.ForeignKey('keyword.id'), nullable = True)
    logo_id = db.Column(db.Integer, db.ForeignKey('logo.id'), nullable = True)
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable = True)