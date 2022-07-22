from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databese.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'secret'

class Linguagens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route('/')
def index():
  linguagens = Linguagens.query.all()
  return render_template('index.html', linguagens=linguagens)

@app.route('/add', methods=['POST'])
def add():
  name = request.form.get('linguagem')
  new_lin = Linguagens(name=name)
  db.session.add(new_lin)
  db.session.commit()
  return redirect('/')

@app.route('/delete/<int:id>')  
def delete(id):
  linguagem = Linguagens.query.filter_by(id=id).first()
  db.session.delete(linguagem)
  db.session.commit()
  return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
  name = request.form.get('linguagem')
  linguagem = Linguagens.query.filter_by(id=id).first()
  linguagem.name = name
  db.session.commit()
  return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')  
