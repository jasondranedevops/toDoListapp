while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            file =open('data/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('data/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case "show" | "display":
            file = open('data/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            current_todos = [item.title().strip('\n') for item in todos]
            for index, item in enumerate(current_todos):
                print(f"{index + 1}.{item}")

        case "edit":
            file = open('data/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                print(f"{index + 1}.{item}")
            number = int(input("Number of todo to edit: "))
            number = number -1
            new_todo = input("Enter new todo item: ")
            todos[number] = new_todo
            file = open('data/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case "complete":
            file = open('data/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                print(f"{index + 1}.{item}")
            number = int(input("Number of todo to complete: "))
            print(f"{todos[number-1]} was removed from the list.")
            todos.pop(number -1)
            file = open('data/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case "exit":
            break
        case _:
            print("pleas use only add, show, edit, complete or exit")

print("See you soon!")

