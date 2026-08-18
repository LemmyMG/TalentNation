# Create a variable that represents the maximum allowed risk
# instead of hard-coding 2 in the validation

max_risk = 2

continue_program = True

while continue_program:
    try:
        account_size = int(input("\nEnter Account Size: "))
        risk_percentage = float(input("Enter Risk Percentage: "))

        # Validate that both values are greater than zero
        if account_size <= 0 or risk_percentage <= 0:
            print("Invalid number. Values must be greater than 0")
        # Check whether the selected risk is within the 2% limit
        elif risk_percentage > max_risk:
            print(f"\nInvalid risk. Maximum allowed risk is {max_risk}%.")
        else:
            # Calculate the dollar amount being risked
            risk_amount = account_size * risk_percentage / 100

            # Display the trade information
            print("\n========= Risk Summary ========")
            print(f"Account Size: ${account_size}")
            print(f"Risk Percentage: {risk_percentage}%")
            # Format risk amount to two decimal places
            print(f"Risk Amount: ${risk_amount:.2f}")
            
        # Normalize the user's response by removing surrounding spaces
        # and converting it to lowercase.
        while True:   
            answer = input("\nDo you want to perform another trade?:\n")
            answer = answer.strip().lower()  

            if answer == "yes":
                break
            elif answer == "no":
                continue_program = False
                break
            else: 
                print("Please enter yes or no!")
                

    except ValueError:
        print("Please, enter a valid number.")
