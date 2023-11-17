def fizz_buzz(number):
    # Implement the FizzBuzz logic
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

def run_tests():
    test_numbers = [-99, -1, 0, 00, 0.0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 14, 15, 16, 29, 30]

    for number in test_numbers:
        result = fizz_buzz(number)
        print(f"Input: {number}, Result: {result}")
        # Add additional assertions or checks as needed

if __name__ == "__main__":
    run_tests()
