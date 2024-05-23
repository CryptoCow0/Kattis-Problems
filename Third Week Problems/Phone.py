def is_consistent(numbers):
    # Create an empty set to store prefixes
    prefixes = set()
    
    for number in numbers:
        for i in range(1, len(number) + 1):
            prefix = number[:i]
            # Check if the prefix is already in the set
            if prefix in prefixes:
                return "NO"
        # Add the entire number as a prefix
        prefixes.add(number)
    
    return "YES"

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):

    num_numbers = int(input())

    phone_numbers = [input().strip() for _ in range(num_numbers)]
    phone_numbers.sort()
    result = is_consistent(phone_numbers)
    print(result)
