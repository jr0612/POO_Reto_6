def prime_numbers(numbers: list) -> list:
    prime_numbers = []

    def is_prime(number):
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


