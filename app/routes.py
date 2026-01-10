from flask import request, jsonify
from app.models import db, Task

def init_routes(app):
    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([task.to_dict() for task in tasks])

    @app.route('/tasks', methods=['POST'])
    def create_task():
        data = request.json
        new_task = Task(title=data['title'])
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201

    @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204