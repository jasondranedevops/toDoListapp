while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            with open('data/todos.txt', 'r') as file:
                todos = file.readlines()
            with open('data/todos.txt', 'w') as file:
                todos.append(todo)
                file.writelines(todos)

        case "show" | "display":
            with open('data/todos.txt', 'r') as file:
                todos = file.readlines()

            current_todos = [item.title().strip('\n') for item in todos]
            for index, item in enumerate(current_todos):
                print(f"{index + 1}.{item}")

        case "edit":
            file = open('data/todos.txt', 'r')
            with open('data/todos.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                print(f"{index + 1}.{item}")
            number = int(input("Number of todo to edit: "))
            number = number -1
            new_todo = input("Enter new todo item: ")
            todos[number] = new_todo
            with open('data/todos.txt', 'w') as file:
                file.writelines(todos)

        case "complete":
            with open('data/todos.txt', 'r') as file:
                todos = file.readlines()
            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                print(f"{index + 1}.{item}")
            number = int(input("Number of todo to complete: "))
            print(f"{todos[number-1]} was removed from the list.")
            todos.pop(number -1)
            with open('data/todos.txt', 'w') as file:
                file.writelines(todos)

        case "exit":
            break
        case _:
            print("pleas use only add, show, edit, complete or exit")

print("See you soon!")

