from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []
proximo_id = 1


class TaskCreate(BaseModel):
    title: str
    description: str


class Task(BaseModel):
    id: int
    title: str
    description: str
    is_done: bool = False






@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global proximo_id

    nova_task = Task(
        id=proximo_id,
        title=task.title,
        description=task.description
    )

    tasks.append(nova_task)

    proximo_id += 1

    return {
        "message": "Task created successfully",
        "task": nova_task
    }

@app.get("/tasks")
def get_tasks(is_done: bool | None = None):
    if is_done is None:
        return tasks

    return [task for task in tasks if task.is_done == is_done]

@app.get("/tasks/{task_id}", status_code=200)
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", status_code=200)
def update_task(task_id: int, updated_task: TaskCreate):
    for task in tasks:
        if task.id == task_id:
            task.title = updated_task.title
            task.description = updated_task.description
            return {
                "message": "Task updated successfully",
                "task": task
            }
    raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{task_id}/is_done", status_code=200)
def mark_task_done(task_id: int):
    for task in tasks:
        if task.id == task_id:
            if not task.is_done:
                task.is_done = True
                message = "Task marked as done"
            else:
                task.is_done = False
                message = "Task marked as not done"
            return {
                "message": message,
                "task": task
            }
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=200)
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")