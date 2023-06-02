def prime_number(num):
    """
    Check if a number is a prime number.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    elif num >= 2:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False


def nth_prime_number(n):
    """
    Find the nth prime number.

    Args:
        n (int): The position of the prime number to find.

    Returns:
        int: The nth prime number.

    """
    i = 2
    count = 0
    while count < n:
        if prime_number(i):
            count += 1
            if count == n:
                return i
            else:
                i += 1
        else:
            i += 1
    return i


print(nth_prime_number(10001))
