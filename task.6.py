class EuclideanAlgorithm:
    """Compute the GCD and LCM of two integers."""

    def gcd(self, a, b):
        """Compute the GCD using the Euclidean Algorithm."""
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        """Compute the Least Common Multiple (LCM) using the GCD."""
        return abs(a * b) // self.gcd(a, b)

def get_input(prompt):
    """This function prompts the user for input and checks for non-negative integers."""
    while True:
        try:
            # Obtain input and attempt to convert it to an integer
            value = int(input(prompt))
            # Check if the integer is non-negative
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            # Catch the ValueError if the input is not an integer
            print("Invalid input. Please enter a non-negative integer.")

euclidean = EuclideanAlgorithm()  # Create an instance of the EuclideanAlgorithm class

# Get user input for the two numbers
print("Calculation using the Euclidean Algorithm.")
number1 = get_input("Enter the first non-negative integer: ")
number2 = get_input("Enter the second non-negative integer: ")

# Calculate and print the GCD
gcd_result = euclidean.gcd(number1, number2)
print(f"The GCD of {number1} and {number2} is: {gcd_result}")

# Calculate and print the LCM
lcm_result = euclidean.lcm(number1, number2)
print(f"The LCM of {number1} and {number2} is: {lcm_result}")