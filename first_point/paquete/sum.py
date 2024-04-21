def max_consecutive_sum(numbers: list) -> int:
    sum_numbers: int = 0
    sum_numbers += max(numbers)
    if max(numbers) == numbers[-1]:
        sum_numbers += numbers[numbers.index(max(numbers))-1]
        return sum_numbers

    elif numbers[numbers.index(max(numbers))+1] > numbers[numbers.index(max(numbers))-1]:
        sum_numbers += numbers[numbers.index(max(numbers))+1]
        return sum_numbers

    else:
        sum_numbers += numbers[numbers.index(max(numbers))-1]
        return sum_numbers