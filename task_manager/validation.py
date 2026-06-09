from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str) or title.strip() == "":
        return False, "Task title cannot be empty."
    return True, ""


def validate_task_description(description):
    if not isinstance(description, str) or description.strip() == "":
        return False, "Task description cannot be empty."
    return True, ""


def validate_due_date(due_date):
    if not isinstance(due_date, str) or due_date.strip() == "":
        return False, "Due date cannot be empty."

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format."