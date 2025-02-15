#Question 2  
bill_amount = float(input("Enter bill amount: $"))
tip_percentage = int(input("Enter tip amount: (%)"))


tip_amount = (tip_percentage / 100) * bill_amount
total = bill_amount + tip_amount



print(f"\nBill Amount: ${bill_amount:.2f}")
print(f"Tip ({tip_percentage}%): ${tip_amount:.2f}")
print(f"Total Amount: ${total:.2f}")
print("---------------------")

