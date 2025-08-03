# Simple Rent Calculator in Python

# Define the necessary variables
rent_amount = float(input("Enter the monthly rent amount: "))
months = int(input("Enter the number of months: "))

# Calculate total rent
total_rent = rent_amount * months

# Display the result
print(f"Total rent for {months} months is: ${total_rent:.2f}")