from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:password@localhost/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qoqokxliesbuey:2dabcd90efbb88737c4a0d47aa4ca7bf0a621f800efb8312d1cef4180141cbea@ec2-54-235-181-120.compute-1.amazonaws.com:5432/d2mhrl51519nil?sslmode=require'
db = SQLAlchemy(app)


class Data(db.Model):
  __tablename__ = "data"
  id = db.Column(db.Integer, primary_key=True)
  email_ = db.Column(db.String(120), unique=True)
  height_ = db.Column(db.Integer)

  def __init__(self, email_, height_):
    self.email_ = email_
    self.height_ = height_



@app.route("/")
def index():
  return render_template("index.html")




@app.route("/success", methods=['POST'])
def success():
  if request.method == 'POST':
    email = request.form["email_name"]
    height = request.form["height_name"]
    print(email, height)
    print(request.form)
  
    if db.session.query(Data).filter(Data.email_==email).count() == 0:
      data = Data(email, height)
      db.session.add(data)
      db.session.commit()

      average_height = db.session.query(func.avg(Data.height_)).scalar()
      average_height = round(average_height, 2)
      count = db.session.query(Data.height_).count()
      send_email(email, height, average_height, count)

      return render_template('success.html')
  return render_template('index.html', 
    text="Seems like we've got something from that email address.")

if __name__ == '__main__':
  app.debug = True
  app.run()