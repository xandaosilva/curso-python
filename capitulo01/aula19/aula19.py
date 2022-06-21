texto = "Aprendendo a programar em Python"
texto_gerado = ""

for n, caractere in enumerate(texto):
    print(n, caractere)

for numero in range(0, 12, 1):
    if numero % 2 == 0:
        print(numero)

for letra in texto:
    if letra == "t" or letra == "h":
        texto_gerado += letra.upper()
    else:
        texto_gerado += letra

print(texto_gerado)