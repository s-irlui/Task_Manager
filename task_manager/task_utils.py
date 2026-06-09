from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def add_task(tasks, title, description, due_date):
    valid_title, title_error = validate_task_title(title)
    if not valid_title:
        print(title_error)
        return

    valid_description, description_error = validate_task_description(description)
    if not valid_description:
        print(description_error)
        return

    valid_due_date, due_date_error = validate_due_date(due_date)
    if not valid_due_date:
        print(due_date_error)
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    print("Task added successfully.")


def mark_task_as_complete(tasks, task_number):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
        return

    tasks[task_number - 1]["completed"] = True
    print("Task marked as complete.")


def view_pending_tasks(tasks):
    pending_tasks = []

    for task in tasks:
        if task["completed"] == False:
            pending_tasks.append(task)

    if len(pending_tasks) == 0:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")
    for index, task in enumerate(pending_tasks, start=1):
        print(f"{index}. {task['title']}")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")


def calculate_progress(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        return

    completed_count = 0

    for task in tasks:
        if task["completed"] == True:
            completed_count += 1

    progress = (completed_count / len(tasks)) * 100
    print(f"Progress: {progress:.2f}% completed")