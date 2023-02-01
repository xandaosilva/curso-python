from sales import calc_prices

price_a = 49.90
price_b = calc_prices.increase_price(price_a, 15, formata=True)
price_c = calc_prices.decrease_price(price_a, 15, formata=True)

print(price_b)
print(price_c)
