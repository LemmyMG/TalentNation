# Get the account size and risk percentage from the user
try:
    account_size = int(input("Enter Account Size: "))
    risk_percentage = int(input("Enter Risk Percentage: "))
# Calculate the dollar amount being risked
        
    risk_amount = account_size * risk_percentage / 100

# Display the trade information
    print("\n========= Risk Summary ========")
    print(f"Account Size: ${account_size}")
    print(f"Risk Percentage: {risk_percentage}%")
    print(f"Risk Amount: ${risk_amount}")

# Check whether the selected risk is within the 2% limit
    print("=== === === === == ==== ==== ==")
    if risk_percentage <= 2 :
            print("Risk Status: ACCEPTABLE")
    else:
            print("Risk Status: TOO HIGH")
    print("=== === === === === ==== === ==")
    
except ValueError:
    print("Please, enter a valid number.")
      

