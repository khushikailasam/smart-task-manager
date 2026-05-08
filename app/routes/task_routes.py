from flask import Blueprint, request, jsonify

from app import db, socketio
from app.models import Task

task_bp = Blueprint("tasks", __name__)


# ADD TASK
@task_bp.route("/tasks", methods=["POST"])
def add_task():

    data = request.get_json()

    new_task = Task(
        title=data.get("title"),
        description=data.get("description"),
        priority=data.get("priority"),
        status=data.get("status"),
        user_id=data.get("user_id")
    )

    db.session.add(new_task)
    db.session.commit()
    socketio.emit(
    "task_notification",
    {
        "message": "New task added successfully"
    }
)

    return jsonify({
        "message": "Task added successfully"
    }), 201


# GET ALL TASKS
@task_bp.route("/tasks", methods=["GET"])
def get_tasks():

    tasks = Task.query.all()

    task_list = []

    for task in tasks:
        task_list.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status,
            "created_date": task.created_date,
            "user_id": task.user_id
        })

    return jsonify(task_list), 200


# UPDATE TASK
@task_bp.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):

    task = Task.query.get(id)

    if not task:
        return jsonify({
            "message": "Task not found"
        }), 404

    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.priority = data.get("priority", task.priority)
    task.status = data.get("status", task.status)

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully"
    }), 200


# DELETE TASK
@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    task = Task.query.get(id)

    if not task:
        return jsonify({
            "message": "Task not found"
        }), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    }), 200