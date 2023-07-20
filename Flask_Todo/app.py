from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)  # creating the Flask class object
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
# app.config('SQLALCHEMY_TRACK_MODIFICATIONS')=False
db = SQLAlchemy(app)

app.app_context().push()


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    timecreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}\n"


@app.route('/')  # decorator drfines the
def home():
    return "Go to /test for Todo Page"


@app.route('/products')
def products():
    return "This is products page"


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('test.html', allTodo=allTodo)


@app.route('/show')
def show():
    allTodo = Todo.query.all()
    print(allTodo)
    return "This is show page"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
