import math


def find_factors(N, a, r):
    """
    Find non-trivial factors of N using the period r.
    """

    # Shor's algorithm requires an even period
    if r is None or r % 2 != 0:
        return None

    # Calculate a^(r/2) mod N
    x = pow(a, r // 2, N)

    # If x = -1 mod N, this attempt fails
    if x == N - 1:
        return None

    factor1 = math.gcd(x - 1, N)
    factor2 = math.gcd(x + 1, N)

    # Check that the factors are non-trivial
    if factor1 in (1, N) or factor2 in (1, N):
        return None

    return factor1, factor2


# Example
N = 15
a = 2
r = 4

factors = find_factors(N, a, r)

print("Number N:", N)
print("Base a:", a)
print("Period r:", r)
print("Factors:", factors)
