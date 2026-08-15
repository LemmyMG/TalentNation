# Trade Risk Calculator — Risk Validation
account_size = 1000
risk_percentage = 2

# Calculate the dollar amount at risk
risk_amount = account_size * risk_percentage / 100

# Display the trade risk information
print("========= Risk Summary ========")
print(f"Account Size: ${account_size}")
print(f"Risk Percentage: {risk_percentage}%")
print(f"Risk Amount: ${risk_amount}")

# Check whether the selected risk is within the 2% limit
print("=== === == == ==== === ===")
if risk_percentage <= 2 :
    print("Risk Status: ACCEPTABLE")
else:
    print("Risk Status: TOO HIGH")
print("=== === == == ==== === ===")
