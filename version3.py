# Read single set of inputs from file
with open("input_single.txt", "r") as file:
    data = file.readline().split()
    a, b, c, x = map(float, data)

# Calculate the weather parameter (y)
y = a * x**2 + b * x + c
print(f"Weather parameter (single file input): {y}")
