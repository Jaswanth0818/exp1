# Input coefficients and time from the keyboard
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
x = float(input("Enter the time (x): "))

# Calculate the weather parameter (y)
y = a * x**2 + b * x + c
print(f"Weather parameter (keyboard input): {y}")
