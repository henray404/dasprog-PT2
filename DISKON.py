eligible_discount = 0.20
sales_tax = 0.05

total_purchases = float(input("input total purchase "))
student = input("are you a student? yes/no ").strip().lower()

if student == "yes":
    discount = eligible_discount * total_purchases
    total = total_purchases - discount
    print(f"Total purchases: ${total_purchases:.2f}")
    print(f"Student's discount (20%): {discount:.2f}")
    print(f"Discounted total: ${total:.2f}")

else:
    total = total_purchases
    print(f"total purchases: ${total:.2f}")


tax_total = total * sales_tax
total = total + tax_total


print(f"Sales tax (5%): ${tax_total:.2f}")
print(f"total: ${total:.2f}")
