def get_todos():
    with open('data/todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def write_todos():
    with open('data/todos.txt', 'w') as file:
        todos.append(todo + "\n")
        file.writelines(todos)
    return todos

def edit_todo():
    todos[number] = new_todo + '\n'
    with open('data/todos.txt', 'w') as file:
        file.writelines(todos)
    return todos

def list_todos():
    current_todos = [item.title().strip('\n') for item in todos]
    for index, item in enumerate(current_todos):
        print(f"{index + 1}.{item}")
    return todos


while True:
    user_action = input("Type new or add, show or display, edit, complete or done or exit or 'close: ").strip()

    # Check for valid user input
    #valid_actions = ['new', 'add', 'display', 'show', 'done', 'edit', 'complete', 'exit', 'close']
    if user_action.startswith("add") or user_action.startswith("new"):
        todos = get_todos()
        if len(user_action) > 4:
            todo = user_action[4:]
            todos = write_todos()
        else:
            todo = input("Enter a todo: ")
            todos = write_todos()
        print(f"{todo} added to list.")

    elif user_action.startswith("show") or user_action.startswith("display"):
        todos = get_todos()
        todos = list_todos()

    elif user_action.startswith("edit"):
        if len(user_action) > 5:
            number = int(user_action[5:]) -1
            new_todo = input("Enter new todo item: ")
            todos = edit_todo()
            print(f"To Do list item numbered {number + 1}. updated to {new_todo}")
        else:
            todos = get_todos()
            todos = list_todos()
            number = int(input("Number of todo to edit: "))
            if number > len(todos) or number < 1:
                print(f"To Do list does not contain and item numbered {number}. Try again")
                continue
            else:
                number = number - 1
                new_todo = input("Enter new todo item: ")
                todos = edit_todo()
                print(f"To Do list item numbered {number + 1}. updated to {new_todo}")


    elif user_action.startswith("complete") or user_action.startswith("done"):
        todos = get_todos()
        todos = list_todos()
        number = int(input("Number of todo to complete: "))
        try:
            print(f"{todos[number-1]} was removed from the list.")
            todos.pop(number - 1)
            with open('data/todos.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print(f"To Do list does not contain an item numbered {number}. Try again")
            continue

    elif user_action.startswith("exit") or user_action.startswith("close"):
        break

    else:
        print("Please use only type new or add, show or display, edit, complete or done or exit or close: ")

print("See you soon!")
