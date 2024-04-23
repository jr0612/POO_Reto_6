def basic_operation(first_number: int, second_number: int, sign: chr):
    match sign:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number
        case "/":
            try:
                return first_number / second_number
            except ZeroDivisionError:
                return "Math ERROR"
        case _:
            return "invalid operation"
            # * adding the default case of match statement


def perform_operation(first_number: int, second_number: int, sign: chr):
    """
    Catching the TypeError
    """
    try:
        return basic_operation(first_number, second_number, sign)
    except TypeError:
        return "Invlid input type"


"""
Trying better coments:
#* important information
#! warning
# ? questions
# todo
"""

print(perform_operation(1, "6", "+"))

