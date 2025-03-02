from flask import render_template, url_for, flash, redirect, request
from app import app, db
from app.models import Task
from app.forms import TaskForm

@app.route('/')
def home():
    tasks = Task.query.all()
    return render_template('home.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit', methods=['POST'])
def edit_task():
    task_id = request.form['id']
    task = Task.query.get(task_id)
    task.title = request.form['title']
    task.description = request.form['description']
    db.session.commit()
    return redirect(url_for('home'))