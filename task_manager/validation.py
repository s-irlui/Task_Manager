from datetime import datetime


def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Task title cannot be empty")
    return True


def validate_task_description(description):
    if len(description) == 0:
        raise ValueError("Task description cannot be empty")
    return True


def validate_due_date(due_date):
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format")

    return True