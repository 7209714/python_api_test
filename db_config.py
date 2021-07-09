from flaskext.mysql import MySQL
import flask

mysql = MySQL() 

app = flask.Flask(__name__)
# MySQL 配置
app.config['MYSQL_DATABASE_USER'] = 'root' 
app.config['MYSQL_DATABASE_PASSWORD'] = '' 
app.config['MYSQL_DATABASE_DB'] = 'apiuser' 
app.config['MYSQL_DATABASE_HOST' ] = 'localhost' 
mysql.init_app(app)
