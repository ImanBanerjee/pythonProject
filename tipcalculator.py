# bill input
bill = input("Enter the bill amount: $")


# Remove dollar sign and leading/trailing whitespaces
bill_amount = bill.replace('$', '').strip() # strip () to remove railing whitespaces (learned from
# google



# Convert the cleaned string to an integer
amount = float(bill_amount)

print(f"some suggestions : \n15% - {amount*(15/100):.2f}\n17% - {amount*(17/100):.2f}\n18% - {amount*(18/100):.2f}")
# bill input

percentage = input("Enter the Tip amount: %")

# Remove percentage sign and leading/trailing whitespaces
percent_amount = percentage.replace('%', '').strip()

percent = float(percent_amount)


tip = float(amount * (percent/100)) #tip ammount

total = float(amount + tip) # total amount with tip

# Print or return the result
print(f"Tip Amount is ${tip:.2f}\nTotal amount with tip is ${total:.2f}")


