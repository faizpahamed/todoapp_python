def get_todo_list():
    with open("Files/todo.txt","r") as file:
        tolist = file.readlines()
    return tolist

def write_to_todolsit(todos):
    with open("Files/todo.txt", "w") as file:
        file.writelines(todos)

def add_to_todo_list(todoitem):
    tolist = get_todo_list()
    with open("Files/todo.txt","w") as file:
        tolist.append(todoitem)
        file.writelines(tolist)
