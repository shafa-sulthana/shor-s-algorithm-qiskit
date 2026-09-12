import math


def gcd(a, b):
    return math.gcd(a, b)


def modular_power(a, exponent, N):
    return pow(a, exponent, N)


def find_period(a, N):
    """
    Find the smallest positive r such that:
        a^r mod N = 1
    """

    value = 1

    for r in range(1, N * N):
        value = (value * a) % N

        if value == 1:
            return r

    return None


# Example
N = 15
a = 2

print("Number N:", N)
print("Base a:", a)
print("gcd(a, N):", gcd(a, N))
print("Period r:", find_period(a, N))
