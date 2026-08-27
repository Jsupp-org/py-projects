total = 0.0
totalItems = 0
 
name = input("Customer Name: ")
 
while True:
    item_Name = input("\nEnter item name (type 'done' if finished): ")

    if item_Name.lower() == "done":
        print("Thank you for shopping with us!")
        break
     
    while True:
        item_Price = input(f"Enter {item_Name} price: ")
        try:
            item_Price = float(item_Price)
            if item_Price >= 0:
                break
            else:
                print("Please enter a valid price")
        except ValueError:
            print("Please enter a valid price")

    while True:
        qty = input("Quantity: ")
        if qty.isdigit() and int(qty) > 0:
            qty = int(qty)
            break
        else:
            print("Please enter a valid number")
 
    subtotal = item_Price * qty
    print(f"\nSubtotal: P{subtotal:,.2f}")
    total += subtotal
    totalItems = totalItems + qty
 
discount = 0.0
if total >= 1000:
    discount = total * 0.10
 
finalAmount = total - discount
 
 
print("\n============================")
print("Customer Name:",name)
print("Number of Items Purchased:", totalItems)
print(f"Total Amount: P{total:,.2f}")
print(f"Discount: P{discount:,.2f}")
print(f"Final Amount to Pay: P{finalAmount:,.2f}")
print("============================")
 
 
