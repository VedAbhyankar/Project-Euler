# nth triangular number is n(n+1)/2

def factors(n: int):
    """
    Input:
            n: integer n to be factored:

    Output:
            factors: list of factors of n
    """

    assert n != 0
        
    if n == 1:
        return [1]

    factors = set({})

    i = 1
    # atleast one factor in every unique factor pair <= sqrt(n)
    while i**2 <= abs(n): 
        if n % i == 0:
            # append factor pair
            factors.add(i)  
            factors.add(n // i)
        i += 1
    
    factors = list(factors)

    if n < 0:
        for f in factors.copy():
            factors.append(-1 * f)
    
    return factors

def triangular_number(n: int):
    """
    Input:
            n: index of triangular number to be returned
    
    Output:
            triangular_number: nth triangular number
    """
    
    assert n >= 0
    
    return (n * (n + 1)) / 2

threshold = 500

ans = 1
i = 1

while len(factors(ans)) <= threshold:
    ans = triangular_number(i)
    i += 1

print(f"\nFirst triangular number with more than {threshold} factors: {ans}")