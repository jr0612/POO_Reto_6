def max_consecutive_sum(numbers: list) -> int:
    if not isinstance(numbers, list):
        # * raising an error for non list
        raise TypeError("Input must be a list")
    if not numbers:
        # * rasing an error for empty list
        raise ValueError("List is empty")
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


print(max_consecutive_sum([1, 2, 3, 4, 5]))
print(max_consecutive_sum([1, 2, 3, "4", 4]))
