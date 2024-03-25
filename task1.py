def gcd(self, a, b):
    # Continue the loop until b becomes 0
    while b != 0:
        # Replace a with b and b with the remainder of a divided by b
        a, b = b, a % b
        # When b is 0, a contains the GCD
    return a

#example
result = gcd(270, 192)# Calculate the GCD

print(f"The GCD of 270 and 192 is:{result}")# Print the result