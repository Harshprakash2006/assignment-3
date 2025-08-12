import math
# Step 1: Ask the user for a number
num = float(input("Enter a number: "))

# Step 2: Perform calculations using math module
sqrt_num = math.sqrt(num)              # Square root
log_num = math.log(num)                # Natural logarithm (base e)
sine_num = math.sin(num)               # Sine (input in radians)

# Step 3: Display results
print(f"Square root: {sqrt_num}")
print(f"Logarithm: {log_num}")
print(f"Sine: {sine_num}")