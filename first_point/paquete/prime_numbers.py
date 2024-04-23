def prime_numbers(numbers: list) -> list:
    if not isinstance(numbers, list):
        raise TypeError("The input must be list")
        #  raising an error for non-list input
    if not numbers:
        raise ValueError("The input list is empty")
        #  raising and error for empty list
    prime_numbers = []

    def is_prime(number):
        if not isinstance(number, int):
            raise TypeError("The input must be integer")
            # raising an error for non-integer input

        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for x in range(3, number, 2):
            if number % x == 0:
                return False
        return True

    for number in numbers:
        if is_prime(number) is True:
            prime_numbers.append(number)
    return prime_numbers


try:
    print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, "10"]))
#    print(prime_numbers([]))
#    print(prime_numbers(5))
#    print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))

except (TypeError, ValueError) as e:
    print("Error:", e)

try:
    print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
except (TypeError, ValueError) as identifier:
    print("Error:", identifier)
