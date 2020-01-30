from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()

id = 0


def increment_id():
    global id
    id = id + 1
    return id


todo_list = []


class Todo(BaseModel):
    id = 0
    todo: str
    in_progress = True


@app.get("/")
def view_todos():
    """
    Returns a list of all todos.
    """
    return todo_list


@app.get("/in-progress")
def view_in_progress():
    """
    Returns a list of all todos that are still in progress.
    """
    return list(filter(lambda todo: todo["in_progress"], todo_list))


@app.get("/completed")
def view_completed():
    """
    Returns a list of all todos that are completed.
    """
    return list(filter(lambda todo: not todo["in_progress"], todo_list))


@app.get("/{id}")
def view_todo_by_id(id: int):
    """
    Takes a todo ID as a route parameter and a single todo matching the ID.
    """
    return list(filter(lambda todo: todo["id"] == id, todo_list))


@app.post("/add-todo", status_code=201)
def add_todo(todo: Todo):
    """
    Adds a todo to the todo_list list
    """
    todo.id = increment_id()
    todo_list.append(todo.dict())
    return Response("Todo added")


@app.put("/{id}/completed")
def mark_complete(id: int):
    """
    Takes a todo ID as a route parameter and changes the value of
    'in_progress' to 'False'.
    """
    for todo in todo_list:
        if todo["id"] == id:
            todo["in_progress"] = False
    return Response("Todo marked 'completed'")


@app.put("/{id}/in-progress")
def mark_in_progress(id: int):
    """
    Takes a todo ID as a route parameter and changes the value of
    'in_progress' to 'True'.
    """
    for todo in todo_list:
        if todo["id"] == id:
            todo["in_progress"] = True
    return Response("Todo marked 'in progress'")


@app.delete("/all/delete")
def delete_all():
    """
    Deletes all todos from todo_list list
    """
    todo_list.clear()
    return Response("Todo list cleared")


@app.delete("/{id}/delete")
def delete_todo(id: int):
    """
    Takes a todo ID as a route parameter and deletes the todo item.
    """
    for todo in todo_list:
        if todo["id"] == id:
            todo_list.remove(todo)
        else:
            return Response(f"Todo with id:{id} not found", status_code=404)
    return Response(f"Todo with id:{id} deleted")
