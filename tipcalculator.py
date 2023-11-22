# Get user input
bill = input("Enter the bill amount: ")
percentage = input("Enter the Tip %: ")

# Remove dollar sign and leading/trailing whitespaces
bill_ammount = bill.replace('$', '').strip() # strip () to remove railing whitespaces (learned from
# google


# Remove percentage sign and leading/trailing whitespaces
percent_ammount = percentage.replace('%', '').strip()


# Convert the cleaned string to an integer
ammount = int(bill_ammount)

percent = int(percent_ammount)


tip = int(ammount * (percent/100)) #tip ammount

total = int(ammount + tip) # total ammount with tip

# Print or return the result
print(f"Tip Ammount is {tip} and Total ammount with tip is {total}")


