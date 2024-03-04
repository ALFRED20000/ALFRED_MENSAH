print("Welcome to Asanka Hotel")
try:
    totalfoodpurchased = float(input(" Enter the amount of your food charge: "))
except ValueError:
    print("Invalid Input: Please Input Amount in numeric values")
    exit()
tip = round(float(totalfoodpurchased * 0.18))
print(f" Tip $: {tip}")
tax =  round(float(int(totalfoodpurchased)/100*7))
print(f" Sales Tax $: {tax}")
totalPurchased = (totalfoodpurchased+ tip + tax)
print(f"Grand Total $: { totalPurchased}")