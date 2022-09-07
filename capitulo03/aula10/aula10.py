string_a = "0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789"
aux = 10
list_a = [string_a[i:i+aux] for i in range(0, len(string_a), aux)]
string_b = ".".join(list_a)

print(list_a)
print(string_b)
