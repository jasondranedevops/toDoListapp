while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    # Check for valid user input
    valid_actions = ['add', 'show', 'edit', 'complete', 'exit']

    if "add" in user_action:
        with open('data/todos.txt', 'r') as file:
            todos = file.readlines()

        if len(user_action) > 4:
            todo = user_action[4:] + "\n"
            with open('data/todos.txt', 'w') as file:
                todos.append(todo)
                file.writelines(todos)
        else:
            todo = input("Enter a todo: ") + "\n"
            with open('data/todos.txt', 'w') as file:
                todos.append(todo)
                file.writelines(todos)



    elif "show" in user_action or "display" in user_action:
        with open('data/todos.txt', 'r') as file:
            todos = file.readlines()

        current_todos = [item.title().strip('\n') for item in todos]
        for index, item in enumerate(current_todos):
            print(f"{index + 1}.{item}")

    elif "edit" in user_action:
        with open('data/todos.txt', 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1}.{item}")
        number = int(input("Number of todo to edit: "))
        number = number - 1
        new_todo = input("Enter new todo item: ")
        todos[number] = new_todo
        with open('data/todos.txt', 'w') as file:
            file.writelines(todos)

    elif "complete" in user_action:
        with open('data/todos.txt', 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip('\n').title()
            print(f"{index + 1}.{item}")
        number = int(input("Number of todo to complete: "))
        print(f"{todos[number-1]} was removed from the list.")
        todos.pop(number - 1)
        with open('data/todos.txt', 'w') as file:
            file.writelines(todos)

    elif "exit" in user_action:
        break

    else:
        print("Please use only add, show, edit, complete or exit")

print("See you soon!")
