def error_for_list_title(title, lists):
    if any(lst["title"] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters."
    else:
        return None

def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst["id"] == list_id), None)

def error_for_todo_item(todo):
    if not 1 <= len(todo) <= 100:
        return "The todo title must be between 1 and 100 characters."
    else:
        return None
    
def find_todo_by_id(todo_id, todos):
    return next((todo for todo in todos if todo["id"] == todo_id), None)

def delete_todo_by_id(todo_id, lst):
    todo = find_todo_by_id(todo_id, lst["todos"])
    todo_idx = lst["todos"].index(todo)
    lst["todos"].pop(todo_idx)
    return None

def mark_all_completed(lst):
    for todo in lst["todos"]:
        todo["completed"] = True
    return None

def todos_remaining(lst):
    return sum(1 for todo in lst["todos"] if not todo["completed"])

def is_list_completed(lst):
    return len(lst["todos"]) > 0 and todos_remaining(lst) == 0

def sort_items(items, select_completed):
    sorted_items = sorted(items, key=lambda item: item["title"].casefold())

    incomplete_items = [item for item in sorted_items 
                        if not select_completed(item)]
    complete_items = [item for item in sorted_items if select_completed(item)]
    
    return incomplete_items + complete_items

def is_todo_completed(todo):
    return todo["completed"]

def sort_todos(todos):
    sorted_todos = sorted(todos, key=lambda t: t["title"].casefold())

    incomplete_todos = [todo for todo in sorted_todos 
                        if not is_todo_completed(todo)]
    complete_todos = [todo for todo in sorted_todos if is_todo_completed(todo)]
    
    return incomplete_todos + complete_todos