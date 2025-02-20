from flask import Flask, request, jsonify
from app import app, db
from app.models import Task

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    if not title or not description:
        return jsonify({'error': 'Missing required parameters'}), 400

    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task added successfully'}), 200

@app.route('/edit', methods=['POST'])
def edit_task():
    task_id = request.form.get('id')
    title = request.form.get('title')
    description = request.form.get('description')
    if not task_id or not title or not description:
        return jsonify({'error': 'Missing required parameters'}), 400

    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    task.title = title
    task.description = description
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'}), 200