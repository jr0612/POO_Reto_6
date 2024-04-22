# POO_Reto_6 🔷:
## First point
Add the required exceptions in the Reto 1 code assigments.
### basic operations
#### original code:
```python
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
```
For this code assigment I made the fallowing changes:
- A default case was added in the match statement:
  ```python
  case _:
    return 'invalid operation' #* adding the default case of match statement
  ```
- The ZeroDivisionError was implemented in the division case
  ```python
  case  "/":
    try:
        return first_number / second_number 
    except ZeroDivisionError:
         return "Math ERROR" 
  
  ```
- The function perform_operation was implemented with an exception of the TypeError.:
  ```python
  def perform_operation(first_number: int , second_number: int, sing: chr):
    '''
    Catching the TypeError
    '''
    try:
        return basic_operation(first_number,second_number,sing)
    except TypeError:
        return "Invlid input type"
  ```
#### code after changes
```python
def basic_operation(first_number: int,  second_number: int, sign: chr):
    match sign:
        case  "+":
            return first_number + second_number
        case  "-":
            return first_number - second_number
        case  "*":
            return first_number * second_number
        case  "/":
            try:
                return first_number / second_number 
            except ZeroDivisionError:
                 return "Math ERROR"   
        case _:
            return 'invalid operation' #* adding the default case of match statement
        
def perform_operation(first_number: int , second_number: int, sign: chr):
    '''
    Catching the TypeError
    '''
    try:
        return basic_operation(first_number, second_number, sign)
    except TypeError:
        return "Invlid input type"
```
  

## Second point
In the package `Shape` identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.
