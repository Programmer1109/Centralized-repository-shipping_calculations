# Here is a an update by Programmer 1109
# Here is the latest update by Programmer 1109
# Shipping Cost Calculator

print("Calculating Shipping Costs")
## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

