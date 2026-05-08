const socket = io();

socket.on("task_notification", (data) => {
    alert(data.message);
});


async function loadTasks() {

    const response = await fetch("/tasks");
    const tasks = await response.json();

    const taskList = document.getElementById("taskList");

    taskList.innerHTML = "";

    tasks.forEach(task => {

        taskList.innerHTML += `
            <div class="task-card">

                <h3>${task.title}</h3>

                <p>${task.description}</p>

                <p>
                    <strong>Priority:</strong>
                    ${task.priority}
                </p>

                <p>
                    <strong>Status:</strong>
                    ${task.status}
                </p>

                <button onclick="deleteTask(${task.id})">
                    Delete
                </button>

            </div>
        `;
    });
}


async function loadAnalytics() {

    const response = await fetch("/analytics");
    const data = await response.json();

    document.getElementById("totalTasks").innerText =
        data.total_tasks;

    document.getElementById("completedTasks").innerText =
        data.completed_tasks;

    document.getElementById("pendingTasks").innerText =
        data.pending_tasks;

    document.getElementById("completionPercentage").innerText =
        data.completion_percentage + "%";
}


async function addTask() {

    const title =
        document.getElementById("title").value;

    const description =
        document.getElementById("description").value;

    const priority =
        document.getElementById("priority").value;

    const status =
        document.getElementById("status").value;

    await fetch("/tasks", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            title,
            description,
            priority,
            status,
            user_id: 1
        })
    });

    loadTasks();
    loadAnalytics();
}


async function deleteTask(id) {

    await fetch(`/tasks/${id}`, {
        method: "DELETE"
    });

    loadTasks();
    loadAnalytics();
}


loadTasks();
loadAnalytics();