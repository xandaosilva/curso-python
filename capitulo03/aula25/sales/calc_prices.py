from capitulo03.aula25.sales import format_price


def increase_price(value, percent, formata=False):
    r = value + (value*(percent/100))

    if formata:
        return format_price.format_to_real(r)
    else:
        return r


def decrease_price(value, percent, formata=False):
    r = value - (value*(percent/100))

    if formata:
        return format_price.format_to_real(r)
    else:
        return r
