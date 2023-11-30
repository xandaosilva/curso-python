from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-b", "--basic", help="Hello World", type=str, metavar="STRING")

args = parser.parse_args()

res = "Informe o valor de b." if args.basic is None else f"O valor de basic: {args.basic}"

print(res)
