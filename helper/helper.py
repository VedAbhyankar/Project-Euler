
def sum_arithmetic_progression(a: int, n: int, d: int):
    def nth_term_ap(n: int):
        return (a + (n - 1) * d)
    return (int)((n / 2)  * (a + nth_term_ap(n)))