class EuclideanAlgorithm:
    """Compute the GCD of two integers using the Euclidean Algorithm."""
    def gcd(self, a, b):
        # Continue the loop until b becomes 0
        while b != 0:
            # Replace a with b and b with the remainder of a divided by b
            a, b = b, a % b
            # When b is 0, a contains the GCD
        return a

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
#example
euclidean = EuclideanAlgorithm()# Create an instance of the EuclideanAlgorithm class

# Get user input for the two numbers
print("Greatest Common Divisor Calculation using the Euclidean Algorithm.")
number1 = get_input("Enter the first non-negative integer: ")
number2 = get_input("Enter the second non-negative integer: ")

result = euclidean.gcd(number1, number2)
print(f"The GCD of {number1} and {number2} is: {result}")# Print the result