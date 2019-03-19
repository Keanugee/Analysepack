def sum_array(*array):
""" Returns the sum of all values in an array

Args:
    items (array): list or array-like object containing numerical values.

Returns:
    Sum of all values in the given array

Examples:
        >>> sum_array(1,2,3,4,5,6)
        Output = 21
 """
    sum = 0
    for number in array:
        sum+=number
    return sum



def reverse(string):
""" Returns a reversed string

Args:
    item(string): A string

Returns:
    A reversed string

Examples:
        >>> reverse('Hello')
        Output = olleH
"""
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


def factorial(n):
""" factorial (n! = 1×2×3×4×...×n)

Args:
    item(integer): An integer

Returns:
    The Factorial of a number (n!)

Examples:
        >>> factorial(5)
        Output = 120
"""
    result = 1
    count = 2

    while count <= n:
        result = result * count
        count = count + 1

    return result


def fibonacci(n):
"""

"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
