def max_consecutive_sum(numbers: list) -> int:
    """
    a function that takes a list of integers and returns the maximum consecutive sum
    param: list of integers
    return: the maximum consecutive sum
    """

    # ! rasing errors
    if not isinstance(numbers, list):
        # * raising an error for non list
        raise TypeError("Input must be a list")
    if not numbers:
        # * rasing an error for empty list
        raise ValueError("List is empty")
    if not all(isinstance(x, int) for x in numbers):
        # * rasing an error for list with non int
        raise TypeError("List must be integers")

    sum_numbers: int = 0
    sum_numbers += max(numbers)
    if max(numbers) == numbers[-1]:
        sum_numbers += numbers[numbers.index(max(numbers)) - 1]
        return sum_numbers

    elif (
        numbers[numbers.index(max(numbers)) + 1]
        > numbers[numbers.index(max(numbers)) - 1]
    ):
        sum_numbers += numbers[numbers.index(max(numbers)) + 1]
        return sum_numbers

    else:
        sum_numbers += numbers[numbers.index(max(numbers)) - 1]
        return sum_numbers


def perform_max_consecutive_sum(numbers: list):
    try:
        max_consecutive_sum(numbers)
    except (TypeError, ValueError) as e:
        print("error", e)


print(perform_max_consecutive_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(perform_max_consecutive_sum([1, 2, 3, 4, 5, 6, 7, 8, "9", 10]))
print(perform_max_consecutive_sum([]))
print(perform_max_consecutive_sum("hello there"))
