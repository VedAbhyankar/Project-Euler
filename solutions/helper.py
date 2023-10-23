
def sum_arithmetic_progression(a: int, d: int, n: int):
    """
    Input:
            a: first term of arithmetic progression (AP)
            n: term to which AP is to be summed
            d: common difference

    Output:
            sum_arithmetic_progression: sum of first n terms of AP
    """
    assert n >= 1

    sum_arithmetic_progression = (int)((n / 2)  * (2 * a + (n - 1) * d))

    return sum_arithmetic_progression

def nth_term_ap(a: int, d: int, n: int):
    """
    Input:
            a: first term of arithmetic progression (AP)
            n: term to which AP is to be summed
            d: common difference

    Output:
            nth_term_ap: nth term of the AP
    """
    assert n >= 1

    nth_term_ap = a + (n - 1) * d
    
    return nth_term_ap

def factors(n: int):
    """
    Input:
            n: integer n to be factored

    Output:
            factors: list of factors of n
    """

    assert n != 0
        
    if n == 1:
        return [1]

    factors = []

    i = 1
    # atleast one factor in every unique factor pair <= sqrt(n)
    while i ** 2 < abs(n): 
        if n % i == 0:
            # append factor pair
            factors += [i, (n // i)]
        i += 1
    
    if i ** 2 == n:
        factors.append(i)

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

    triangular_number = (n * (n + 1)) / 2
    
    return triangular_number

def gcd(a, b):
    """
    Input:
            a: first integer
            b: second integer
    
    Output:
            triangular_number: nth triangular number
    """    
    assert a  >= 0 and b >= 0
    assert a + b != 0
    
    if a < b:
        a, b = b, a
    
    if b == 0:
        return a
    
    return gcd(b, a % b)

def sum_first_n_powers(n: int, k: int):
    """
    Input:
            n: number to which sum of powers of natural numbers is required
            k: power to which each natural number is raised
    
    Output:
            sum_first_n_powers: sum of kth powers of first n natural numbers
    """
    assert n >= 0
    
    sum_first_n_powers = 0
    
    if k == 1:
        sum_first_n_powers = (n * (n + 1)) / 2
    elif k == 2:
        sum_first_n_powers = (n * (n + 1) * ((2 * n) + 1)) / 6
    elif k == 3:
        sum_first_n_powers = ((n * (n + 1)) / 2) ** 2
    else:
        sum_first_n_powers = sum(i ** k for i in range(n + 1))
    
    return int(sum_first_n_powers)

def n_primes(n: int, return_list = False):
    """
    Input:
            n: index of prime number to be returned 
            return_list: if this is true then list of first n primes is returned
    
    Output:
            n_primes: nth prime number / list of first n primes numbers
    """
    assert n > 0

    n_primes = [2]

    i = 3

    while len(n_primes) != n:

        count = 0

        for prime in n_primes:
            if i % prime == 0:
                break
            count += 1
        
        if count == len(n_primes):
            n_primes.append(i)
        
        i += 1
    
    if not return_list:
        n_primes = n_primes[-1]

    return n_primes

def sieve_of_eratosthenes(n: int):
    """
    Input:
            n: number till which prime numbers are to be found 
    
    Output:
            sieve: bool array till n checks if natural number i (<= n) is prime
    """
    assert n > 0

    from tqdm import tqdm

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    ans = 0

    for i in tqdm(range(2, n + 1)):
        if sieve[i] and (2 * i) <= n:
            for j in range(2 * i, n + 1, i):
                sieve[j] = False
    
    return sieve

def is_prime(n: int):
    """
    Input:
            n: number being tested for primality 
    
    Output:
            is_prime: true if n is prime, false otherwise
    """
    assert n >= 0

    if n <= 3:  # 0, 1 aren't primes; 2, 3 are primes
        return (n > 1)
    if n % 2 == 0 or n % 3 == 0:    # Easy check for further optimization
        return False
        
    # All prime numbers greater than 3 are of form 6k+1 or 6k-1
    if not (n % 6 == 1 or n % 6 == 5):
        return False
    
    i = 5   # Note this is of form 6k-1
    
    while i ** 2 <= n: # go uptil square root

        # use only those 'i' which could be primes themselves
        # i.e. which are +/- 1 mod 6
        # 
        # Since we start with i = 5, check % i and % (i+2) and increment by 6
        # we cover all such potential prime divisors.

        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True
        
if __name__ == "__main__":
    print(factors(int(input())))
