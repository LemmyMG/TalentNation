
try:
    account_size = int(input("Enter Account Size: "))
    risk_percentage = float(input("Enter Risk Percentage: "))

    # Validate that both values are greater than zero
    if account_size <= 0 or risk_percentage <= 0:
        print("Invalid number. Values must be greater than 0")

    else:
        # Calculate the dollar amount being risked
        risk_amount = account_size * risk_percentage / 100

        # Display the trade information
        print("\n========= Risk Summary ========")
        print(f"Account Size: ${account_size}")
        print(f"Risk Percentage: {risk_percentage}%")
        print(f"Risk Amount: ${risk_amount}")

        # Check whether the selected risk is within the 2% limit
        print("=== === === === == ==== ==== ==")

        if risk_percentage <= 2:
            print("Risk Status: ACCEPTABLE")
        else:
            print("Risk Status: TOO HIGH")

        print("=== === === === === ==== === ==")

except ValueError:
    print("Please, enter a valid number.")
