text_a = "Lorem ipsum dolor sit amet"
method = "lower"
value_a = 3

if hasattr(text_a, method):
    print(f"Texto com getattr: {getattr(text_a, method)()}")


if hasattr(value_a, method):
    print(f"Texto modificado: {value_a.method()}")
