from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
# 必须要加载和注册moment，否则页面加载失败，原因待排查。
from flask_moment import Moment


app = Flask('WebExhibition')
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

def create_app():
    app = Flask('WebExhibition')
    app.config.from_pyfile('settings.py')

    db = SQLAlchemy(app)
    bootstrap = Bootstrap(app)
    moment = Moment(app)
    return app

from WebExhibition import views



# body {
#     background-color: rgb(245, 245, 245) !important;
#     background: url("../骑手.gif") ;
#   background-position: center 0; 
#   background-repeat: no-repeat;  
#   background-attachment: fixed; 
#   background-size: cover; 
#   -webkit-background-size: cover;  
#   -o-background-size: cover;  
#   -moz-background-size: cover;  
#   -ms-background-size: cover;
# }