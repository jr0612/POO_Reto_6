def basic_operation(first_number: int,  second_number: int, sign: str):
    match sign:
        case  "+":
            return first_number + second_number
        case  "-":
            return first_number - second_number
        case  "*":
            return first_number * second_number
        case  "/":
            return first_number / second_number