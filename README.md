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
### Prime numbers
#### original code
```python
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


print(prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
```
for this code assigment I made the fallowing changes:
- Type and Value error were raised:
  ```python
      if not isinstance(numbers, list):
        raise TypeError("The input must be list")
        #  * raising an error for non-list input
    if not numbers:
        raise ValueError("The input list is empty")
        #  * raising and error for empty list

  ```
  ```python
          if not isinstance(number, int):
            raise TypeError("The input must be integer")
            # * raising an error for non-integer input

  ```
- The function perform_prime_numbers() was implemented:
  ```python
  def perform_prime_numbers(numbers):
    try:
        """
        adding exeptions for the raised errors
        """
        return prime_numbers(numbers)
    except (TypeError, ValueError) as e:
        print("Error:", e)

  ```
#### code after changes
```python
def prime_numbers(numbers: list) -> list:
    if not isinstance(numbers, list):
        raise TypeError("The input must be list")
        #  * raising an error for non-list input
    if not numbers:
        raise ValueError("The input list is empty")
        #  * raising and error for empty list
    prime_numbers = []

    def is_prime(number):
        if not isinstance(number, int):
            raise TypeError("The input must be integer")
            # * raising an error for non-integer input

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


def perform_prime_numbers(numbers):
    try:
        """
        adding exeptions for the raised errors
        """
        return prime_numbers(numbers)
    except (TypeError, ValueError) as e:
        print("Error:", e)


print(perform_prime_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, "10"]))
print("The execution flow don't stop")

```

### Max consecutive sum
#### original code
```python
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
```
For this code assigment I made the fallowing changes:
- Type and Value error were raised:
  ```python
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
  ```
  - The function perform_max_consecutive_sum() was implementet
    ```python
    def perform_max_consecutive_sum(numbers: list):
    try:
        max_consecutive_sum(numbers)
    except (TypeError, ValueError) as e:
        print("error", e)
    ```

#### code after changes
```python
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
```

### Anagrams
#### original code
```python
def find_anagrams(words: list) -> list:
    anagrams_dict = {}
    for word in words:
        sort_word = "".join(sorted(word))
        if sort_word in anagrams_dict:
            anagrams_dict[sort_word].append(word)
        else:
            anagrams_dict[sort_word] = [word]
    anagrams = [word for group in anagrams_dict.values() if len(group) > 1 for word in group]
    return anagrams
```
For this code assigment I made the fallowing changes:
- Type and Value erros were raised:
  ```python
      # ! raise error
    if not isinstance(words, list):
        # raise error for not list input
        raise TypeError("the input is not a list")
    if not words:
        # raise error for empty list
        raise ValueError("the input list is empty")
    if not all(word.isalpha() for word in words):
        # raise error for non-alphabetic characters
        raise ValueError("the input list contains non-alphabetic characters")
    ```
  - The function perform_find_anagrams() was implementet:
    ```python
    def perform_find_anagrams(words):
    try:
        return find_anagrams(words)
    except Exception as identifier:
        print("error: ", identifier)
    ```
      
  
#### code after changes
```python
def find_anagrams(words: list) -> list:
    """
    a function that finds anagrams from a list of words
    param: words: list
    return: anagrams: list
    """
    # ! raise error
    if not isinstance(words, list):
        # raise error for not list input
        raise TypeError("the input is not a list")
    if not words:
        # raise error for empty list
        raise ValueError("the input list is empty")
    if not all(word.isalpha() for word in words):
        # raise error for non-alphabetic characters
        raise ValueError("the input list contains non-alphabetic characters")

    anagrams_dict = {}
    for word in words:
        sort_word = "".join(sorted(word))
        if sort_word in anagrams_dict:
            anagrams_dict[sort_word].append(word)
        else:
            anagrams_dict[sort_word] = [word]
    anagrams = [
        word for group in anagrams_dict.values() if len(group) > 1 for word in group
    ]
    return anagrams


def perform_find_anagrams(words):
    try:
        return find_anagrams(words)
    except Exception as identifier:
        print("error: ", identifier)


print(perform_find_anagrams(["hello", "world", "hello"]))
print(perform_find_anagrams(["dog", "god", "cat"]))
print(perform_find_anagrams(["ab", "123"]))
print(perform_find_anagrams([]))
print(perform_find_anagrams(134))
```



## Second point
In the package `Shape` identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

### Identification of exceptions cases in the Shape package
Upon reviewing the package, I identified the following cases:
- Exceptions for the creations of Rectangle shapes.
- Exceptions for the creations of Square shapes.
- Exceptions for the creations of all types of Triangles shapes.

### Handling Exceptions in Shape Creation
#### Adding methods in the Shape class
The first step was the creation of the methods create_vertices and create_edges in the Shape class, so they could be inherited for all types of shapes.
#### Implementing Polymorphism Across Shape Types
Then, I proceeded with defining the methods for all the shapes, applying polymorphism.
##### Rectangle
For this shape, I raise the following errors regarding the required data quantity, data type, and their expected formats.
```python
    # todo implement method to set Rectangle vertices correctly
    def create_vertices(self, vertices: list):
        if len(vertices) != 4:
            raise ValueError(
                "Rectangle must have 4 vertices"
            )  # ! raise error if vertices are not 4

        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise TypeError(
                "Rectangle vertices must be Point objects"
                # ! raise error if vertices are not Point objects
            )

        if (
            vertices[0].get_x() == vertices[3].get_x()
            and vertices[0].get_y() == vertices[1].get_y()
            and vertices[1].get_x() == vertices[2].get_x()
            and vertices[2].get_y() == vertices[3].get_y()
        ):
            self.set_vertices(vertices)  # set vertices
        else:
            raise ValueError(
                "Rectangle vertices are not correct"
            )  # raise error if vertices are not correct

    # todo implement method to set Rectangle edges correctly
    def create_edges(self, edges: list):
        if len(edges) != 4:
            raise ValueError(
                "Rectangle must have 4 edges"
            )  # ! raise error if edges are not 4
        if not all(isinstance(edge, Line) for edge in edges):
            raise TypeError(
                "Rectangle edges must be Line objects"
                # ! raise error if edges are not Line objects
            )
        if (
            edges[0].get_length() == edges[2].get_length()
            and edges[1].get_length() == edges[3].get_length()
        ):
            self.set_edges(edges)  # set edges
        else:
            raise ValueError(
                "Rectangle edges are not correct"
            )  # raise error if edges are not correct
```
##### Square
For squares, I adapted the format while preserving the basic errors related to data type and length:
```python
  def create_vertices(self, vertices: list):
        super().create_vertices(vertices)

    def create_edges(self, edges: list):
        super().create_edges(edges)
        if (
            self.get_edges()[0].get_length()
            == self.get_edges()[1].get_length()
            == self.get_edges()[2].get_length()
            == self.get_edges()[3].get_length()
        ):
            self.set_edges(edges)

        else:
            raise ValueError("Square edges are not correct")
```
##### Triangles
For triangles, I initially defined the base errors and then applied polymorphism to all types of triangles. I also handled the length and type of data, and created a frequency dictionary to later confirm if the types of triangles were set correctly:

```python
    # todo implement method to set Triangle vertices correctly
    def create_vertices(self, vertices: list):
        if len(vertices) != 3:
            raise ValueError(
                "Triangle must have 3 vertices"
                # ! raise error if vertices are not 3
            )
        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise TypeError(
                "Triangle vertices must be Point objects"
                # ! raise error if vertices are not Point objects
            )
        side_lengths = [
            vertices[0].compute_distance(vertices[1]),
            vertices[1].compute_distance(vertices[2]),
            vertices[2].compute_distance(vertices[0]),
        ]
        for side_length in side_lengths:
            if (side_length) not in self.frec:
                self.frec[side_length] = 1
            else:
                self.frec[side_length] += 1

    # todo implement method to set Triangle edges correctly
    def create_edges(self, edges: list):
        if len(edges) != 3:
            raise ValueError(
                "Triangle must have 3 edges"
                # ! raise error if edges are not 3
            )
        if not all(isinstance(edge, Line) for edge in edges):
            raise TypeError(
                "Triangle edges must be Line objects"
                # ! raise error if edges are not Line objects
            )
        if self.get_vertices():
            self.set_edges(edges)
        else:
            raise ValueError(
                "Triangle edges are not correct"
                # raise error if edges are not correct
            )

```



After that, I added conditionals for all types of triangles to check their format.

- Isoseles:
  ```python
      def create_vertices(self, vertices: list):
        super().create_vertices(vertices)
        if any(count == 2 for count in self.frec.values()):
            self.set_vertices(vertices)
            return True
        else:
            raise ValueError("Isosceles must have 2 equal sides")
  ```
- Equilateral:
    ```python
        def create_vertices(self, vertices: list):
        super().create_vertices(vertices)
        if all(count == 3 for count in self.frec.values()):
            self.set_vertices(vertices)
            return True
        else:
            raise ValueError("Equilateral must have 3 equal sides")
    ```
- Scalene
    ```python
        def create_vertices(self, vertices: list):
        super().create_vertices(vertices)
        if all(count == 1 for count in self.frec.values()):
            self.set_vertices(vertices)
            return True
        else:
            raise ValueError("Scalene must have 3 unequal sides")
    ```
- TriRectangle:

    With this triangle, I didn't use the frequency dictionary. Instead, I added a new method called create_tri_rectangle. With this method, I checked the inner angles to determine if it was a 90-degree triangle. If it was, I returned True; otherwise, I raised a ValueError:
```python
          def create_tri_rectangle(
        self,
    ):
        if any(inner_angle == 90 for inner_angle in self.get_inner_angles()):
            return True
        else:
            raise ValueError("TriRectangle must have a 90 degree inner angle")

  ```
#### Final step
Finally, I added the corresponding try-except blocks for each shape creation in the main.py file to handle any potential exceptions that may occur during the program's execution.
  
