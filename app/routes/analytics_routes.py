from flask import Blueprint, jsonify
import pandas as pd
import numpy as np

from app.models import Task

analytics_bp = Blueprint("analytics", __name__)


@analytics_bp.route("/analytics", methods=["GET"])
def get_analytics():

    tasks = Task.query.all()

    task_data = []

    for task in tasks:
        task_data.append({
            "status": task.status
        })

    # Create DataFrame
    df = pd.DataFrame(task_data)

    total_tasks = len(df)

    if total_tasks == 0:
        return jsonify({
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "completion_percentage": 0
        })

    completed_tasks = np.sum(df["status"] == "Completed")
    pending_tasks = np.sum(df["status"] == "Pending")

    completion_percentage = (
        completed_tasks / total_tasks
    ) * 100

    return jsonify({
        "total_tasks": int(total_tasks),
        "completed_tasks": int(completed_tasks),
        "pending_tasks": int(pending_tasks),
        "completion_percentage": round(float(completion_percentage), 2)
    })