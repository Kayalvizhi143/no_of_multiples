def count_multiples(array, specific_number):
    if specific_number == 0:
        raise ValueError("The specific number cannot be zero.")
    return sum(num % specific_number == 0 for num in array)

# Get valid input for array
while True:
    try:
        array = list(map(int, input("Enter numbers in the array, separated by spaces or commas: ").replace(',', ' ').split()))
        break
    except ValueError:
        print("Invalid input. Please enter a valid list of integers.")

# Get valid input for specific number
while True:
    try:
        specific_number = int(input("Enter the specific number to check multiples of: "))
        if specific_number != 0:
            break
        print("The specific number cannot be zero. Please enter a non-zero integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Calculate and print the result
try:
    result = count_multiples(array, specific_number)
    print(f"Number of multiples of {specific_number} in the array: {result}")
except ValueError as e:
    print(e)
