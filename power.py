def power(x, n):
    """
    Calculate x raised to the power of n using the specified algorithm.
    
    Args:
        x: A real number (base)
        n: A positive integer (exponent)
    
    Returns:
        The result of x^n
    
    Algorithm:
    1. Initialize P = x, k = 1
    2. While k < n:
       - P = P * x
       - k = k + 1
    3. Return P
    """
    p = x
    k = 1
    
    while k < n:
        p = p * x
        k = k + 1

    return P


if __name__ == "__main__":
    pass 