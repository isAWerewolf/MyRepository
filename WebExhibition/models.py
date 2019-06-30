from WebExhibition import db

class Driving(db.Model):  #表模型
    __tablename__ = 'Driving'
    jia_num = db.Column(db.Integer)
    jian_num = db.Column(db.Integer)
    zhuan_num = db.Column(db.Integer)
    chao_num = db.Column(db.Integer)
    ni_num = db.Column(db.Integer)
    chuang_num = db.Column(db.Integer)
    peng_num = db.Column(db.Integer)
    die_num = db.Column(db.Integer)
    score = db.Column(db.Integer)
    id = db.Column(db.Integer, primary_key=True)
