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
- The ZeroDivisionError was implemented in the division case:
  ```python
  case  "/":
    try:
        return first_number / second_number 
    except ZeroDivisionError:
         return "Math ERROR" 
  
  ```
- The function perform_operation was implemented with an exception of the TypeError:
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
### Palindromes
#### original code:
```python
def is_palindrome(word: str) -> bool:
    flag = True
    if len(word) % 2 != 0:
        for char in range(len(word)):
            if char != (len(word)//2)+1:
                if word[char] != word[-char-1]:
                    flag = False
                    break
    else:
        for char in range(len(word)):
            if word[char] != word[-char-1]:
                flag = False
                break
    return flag
```
For this code assigment I made the fallowing changes:
- The exception for TypeError was added:
  ```python
  def is_palindrome(word: str) -> bool:
    try:
        # implementation here
    except TypeError:               #* Adding the exeption for TypeError 
        return "invalid Input"
  ```
#### code after changes
```python
def is_palindrome(word: str) -> bool:
    try:
        flag = True
        if len(word) % 2 != 0:
            for char in range(len(word)):
                if char != (len(word)//2)+1:
                    if word[char] != word[-char-1]:
                        flag = False
                        break
        else:
            for char in range(len(word)):
                if word[char] != word[-char-1]:
                    flag = False
                    break
        return flag
    except TypeError:               #* Adding the exeption for TypeError 
        return "invalid Input"


print(is_palindrome(123))
```
## Second point
In the package `Shape` identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.
