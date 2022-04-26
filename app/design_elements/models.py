from app.extensions.database import db, CRUDMixin

class Designelement(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key = True)
    slug = db.Column(db.String(80))
    name = db.Column(db.String(80))
    url = db.Column(db.String(2000))

class Logo(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key = True)
    buffer = db.Column(db.Text)
    name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    #designguide_elements = db.relationship('DesignguideElement', backref = 'logo', lazy = True)
    designguide_id = db.Column(db.Integer, db.ForeignKey('designguide.id'), nullable = True)

class Font(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key = True)
    buffer = db.Column(db.Text)
    name = db.Column(db.Text)
    mimetype = db.Column(db.Text)
    #designguide_elements = db.relationship('DesignguideElement', backref = 'font', lazy = True)
    designguide_id = db.Column(db.Integer, db.ForeignKey('designguide.id'), nullable = True)

class Keyword(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    keyword1 = db.Column(db.String(80), nullable = False)
    keyword2 = db.Column(db.String(80), nullable = False)
    keyword3 = db.Column(db.String(80), nullable = False)
    keyword4 = db.Column(db.String(80), nullable = True)
    keyword5 = db.Column(db.String(80), nullable = True)
    keyword6 = db.Column(db.String(80), nullable = True)
    #designguide_elements = db.relationship('DesignguideElement', backref = 'keyword', lazy = True)
    designguide_id = db.Column(db.Integer, db.ForeignKey('designguide.id'), nullable = True)

class Color(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    color1 = db.Column(db.String(20), nullable = False)
    color2 = db.Column(db.String(20), nullable = False)
    color3 = db.Column(db.String(20), nullable = False)
    color4 = db.Column(db.String(20), nullable = True)
    color5 = db.Column(db.String(20), nullable = True)
    color6 = db.Column(db.String(20), nullable = True)
    #designguide_elements = db.relationship('DesignguideElement', backref = 'color', lazy = True)
    designguide_id = db.Column(db.Integer, db.ForeignKey('designguide.id'), nullable = True)
