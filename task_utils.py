try:
    from validation import (
        validate_task_title,
        validate_task_description,
        validate_due_date
    )
except ModuleNotFoundError:
    from task_manager.validation import (
        validate_task_title,
        validate_task_description,
        validate_due_date
    )


tasks = []


def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index, tasks=tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    if index < 1 or index > len(tasks):
        print("Invalid task index.")
        return

    tasks[index - 1]["completed"] = True
    print("Task marked as complete!")


def view_pending_tasks(tasks=tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    for task in tasks:
        if task["completed"] == False:
            print(task)


def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0.0
        return progress

    completed_tasks = 0

    for task in tasks:
        if task["completed"] == True:
            completed_tasks += 1

    progress = (completed_tasks / len(tasks)) * 100
    return progress
