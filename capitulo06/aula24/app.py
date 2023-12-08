from collections import deque

list_numbers_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_numbers_a.append(10)
list_numbers_a.append(11)
last_removed_a = list_numbers_a.pop()

print(f"Último item da lista A removido: {last_removed_a}")
print(f"Lista A de números: {list_numbers_a}")

list_numbers_b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_numbers_b.insert(0, 10)
list_numbers_b.insert(0, 11)
first_removed_b = list_numbers_b.pop(0)

print(f"Primeiro item da lista B removido: {first_removed_b}")
print(f"Lista B de números: {list_numbers_b}")

queue: deque[int] = deque()
queue.append(3)
queue.append(4)
queue.append(5)
queue.appendleft(0)
queue.appendleft(1)
queue.appendleft(2)

print(queue)

queue.pop()
queue.popleft()

print(queue)
