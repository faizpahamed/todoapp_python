import time

from functions import add_to_todo_list,write_to_todolsit,get_todo_list


now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_input = input("Type add,show, edit or exit:")
    user_input = user_input.strip()
    #case add,show,edit,done,exit
    if "add" in user_input:
        todo = user_input[4:]+"\n"
        add_to_todo_list(todo)
    elif "show" in user_input:
        todolist = get_todo_list()
        for index,todo in enumerate(todolist):
            todo = todo.strip("\n")
            print(f"{index +1} - {todo}")
    elif "edit" in user_input:
        item_index_to_edit = int(user_input[5:].strip())-1
        edited_item = input("Enter updated tddo :")
        todolist = get_todo_list()
        todolist[item_index_to_edit] = edited_item
        write_to_todolsit(todolist)
        print("Todo list updated!")
    elif "done" in user_input:
        completed_item_index = int(user_input[5:])-1
        todolist = get_todo_list()
        completed_todo = todolist.pop(completed_item_index)
        print(f"Completed {completed_todo}")
        write_to_todolsit(todolist)

    elif "exit" in user_input:
        print("Exiting the program")
        break
    else:
        print("Invalid Command!!")


