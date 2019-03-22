def sum_array(array):
    sum = 0
    for number in array
        sum+=number
    return sum



def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


def factorial(n):

    result = 1
    count = 2

    while count <= n:
        result = result * count
        count = count + 1

    return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
