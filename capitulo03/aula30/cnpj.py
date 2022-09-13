import re
import random

REGRESSIVES = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def remove_chars(cnpj):
    return re.sub(r"[^0-9]", "", cnpj)


def validate_sequence(cnpj):
    sequence = cnpj[0] * len(cnpj)
    if sequence == cnpj:
        return True
    else:
        return False


def calc(cnpj, digit):
    if digit == 1:
        regressives = REGRESSIVES[1:]
        new_cnpj = cnpj[:-2]
    elif digit == 2:
        regressives = REGRESSIVES
        new_cnpj = cnpj
    else:
        return None

    total = 0

    for index, regressive in enumerate(regressives):
        total += int(cnpj[index]) * regressive

    digit = 11 - (total % 11)
    digit = digit if digit <= 9 else 0
    return f"{new_cnpj}{digit}"


def validate(cnpj):
    cnpj = remove_chars(cnpj)

    try:
        if validate_sequence(cnpj):
            return False
    except:
        return False

    try:
        new_cnpj = calc(cnpj, digit=1)
        new_cnpj = calc(new_cnpj, digit=2)
    except Exception as e:
        return False

    if new_cnpj == cnpj:
        return True
    else:
        return False


def checkvalidate(cnpj):
    if validate(cnpj):
        print(f"{cnpj} é válido.")
    else:
        print(f"{cnpj} é inválido.")


def formatcnpj(cnpj):
    cnpj = remove_chars(cnpj)
    cnpj_formated = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}"
    return cnpj_formated


def generate():
    first_digit = random.randint(0, 9)
    second_digit = random.randint(0, 0)
    third_digit = random.randint(100, 999)
    fourth_digit = random.randint(100, 999)
    fifth_digit = "0001"
    begin_cnpj = f"{first_digit}{second_digit}{third_digit}{fourth_digit}{fifth_digit}00"
    new_cnpj = calc(begin_cnpj, digit=1)
    new_cnpj = calc(new_cnpj, digit=2)

    return formatcnpj(new_cnpj)



