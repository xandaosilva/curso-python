import sys

args = sys.argv

res = "Você não passou argumentos" if len(args) <= 1 else f"Você passou os argumentos {args[1:]}"

print(res)
