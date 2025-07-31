def list_factors(n):
    """
    Get string of factors of n
    :params n is an integer to find factors
    :return string of factors (with a space between each factor)
    >>> list_factors(6)
    '1 2 3 6 '
    >>> list_factors(7)
    '1 7 '
    >>> list_factors(12)
    '1 2 3 4 6 12 '
    """
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(str(i))
    return ' '.join(factors) + ' '


def find_sum_and_num_factors(n):
    """
    Find summation and count number of factors of n
    :params n is an integer to find factors
    :return sum is summation of factors of n
            count is number of factors of n
    >>> find_sum_and_num_factors(6)
    (12, 4)
    >>> find_sum_and_num_factors(7)
    (8, 2)
    >>> find_sum_and_num_factors(12)
    (28, 6)
    """
    factor_sum = 0
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factor_sum += i
            count += 1
    return factor_sum, count

n = int(input("Enter positive number: "))
factors_str = list_factors(n)
factor_sum, factor_count = find_sum_and_num_factors(n)
print(f"Factors of {n} are")
print(factors_str.strip())
print(f"Sum of {factors_str.strip()} is {factor_sum}")
print(f"Number of factors is {factor_count}")
if factor_count == 2:
    print(f"{n} is prime number.")
else:
    print(f"{n} is not prime number.")