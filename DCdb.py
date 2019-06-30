from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for, abort, render_template, flash
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'DrivingConditions.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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

TotalNum = Driving.query.count()
NewestData = Driving.query.get(TotalNum)
print(NewestData.score)

# drivings = Driving.query.all()
# for driving in drivings:
#     print('分数',driving.score,',急加速次数',driving.jia_num,',超速次数',driving.chao_num)


@app.route('/')
def index():
    drivings = Driving.query.all()
    return render_template('base.html', drivings=drivings)

app.run()

