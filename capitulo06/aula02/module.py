def add_items_list(*args):
    list_res: list = []
    for value in args:
        list_res.append(value)
    return list_res


def show_info(*args):
    for arg in args:
        print(arg)

