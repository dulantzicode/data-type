from decimal import Decimal

product_cost = 88.80
commission_rate = 0.08
qty = 450

print(int(product_cost))
print(float(qty))
print(Decimal(product_cost))
print(Decimal("288.830"))
print(complex(commission_rate))

print(type(Decimal("288.830")))