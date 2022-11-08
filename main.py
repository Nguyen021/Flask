from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        content = request.form['content']
        todo = Todo(content=content)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", Tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task = Todo.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task"


@app.route('/update/<int:id>', methods=["POST", "GET"])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task_new = request.form["update_content"]
        task.content = task_new

        db.session.commit()
        return redirect('/')
    else:
        return render_template('update.html', t=task)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
