#  Monthly Sales Report

sales = [
    6000, 4500, 7000, 3000, 8000,
    5500, 4000, 9000, 2000, 6500
]

total_sales = 0
highest_sales = sales[0]
count = 0

for sale in sales:

    total_sales += sale

    if sale > highest_sales:
        highest_sales = sale

    if sale > 5000:
        count += 1

average_sales = total_sales / len(sales)

print("Total Sales =", total_sales)
print("Average Daily Sales =", average_sales)
print("Highest Sales =", highest_sales)
print("Days Above 5000 =", count)