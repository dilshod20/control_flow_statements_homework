def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    n_pos = 0

    if a > 0:
        n_pos += 1
    if b > 0:
        n_pos += 1
    if c > 0:
        n_pos += 1
    
    n_neg = 3 - n_pos
    if n_pos > n_neg:
        return "there are a lot of positive numbers"
    if n_neg > n_pos:
        return "there are a lot of negative numbers"
print(main(-2,4,1))
print(main(3,-3,-6))