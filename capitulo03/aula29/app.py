"""
    add task
    list task
    delete last task (Undo task)
    update last task (redo task)
"""


def show_op(task_list):
    print()
    print("Tarefas:")
    print(task_list)
    print()


def add_task(task, todo_list):
    todo_list.append(task)


def undo_task(todo_list, redo_list):
    if not todo_list:
        print("Nada a desfazer.")
        return

    last_task = todo_list.pop()
    redo_list.append(last_task)


def redo_task(todo_list, redo_list):
    if not redo_list:
        print("Nada para refazer.")
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


if __name__ == "__main__":
    todo_list = []
    redo_list = []

    while True:
        todo = input("Digite uma tarefa ou undo, redo ou ls (desfazer, refazer ou listar): ")

        if todo == "ls":
            show_op(todo_list)
            continue
        elif todo == "undo":
            undo_task(todo_list, redo_list)
            continue
        elif todo == "redo":
            redo_task(todo_list, redo_list)
            continue

        add_task(todo, todo_list)
