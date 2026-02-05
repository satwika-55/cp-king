# Function to compute GCD using the Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute LCM using GCD
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
