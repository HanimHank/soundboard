from app import db

class Sound(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(12), index=True, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    source = db.Column(db.String(120), index=True, unique=True)
    
    def __rept__(self):
        return '<Sound %r>' % (self.label)
        
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), index=True, unique=True)
    sounds = db.relationship('Sound', backref='category', lazy='dynamic')
    
    def __rept__(self):
        return '<Category %r>' % (self.name)
