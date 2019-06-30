from flask import render_template
from WebExhibition import app
from WebExhibition.models import Driving

@app.route('/', methods=['GET', 'POST'])
def index():
    # 加载全记录，按id降序排列
    drivings = Driving.query.order_by(Driving.id.desc()).all()
    # 最新记录
    totalNum = Driving.query.count()
    newestData = Driving.query.get(totalNum)
    return render_template('index.html', drivings=drivings, newestData=newestData)


