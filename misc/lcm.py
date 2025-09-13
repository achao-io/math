def lcm_my_attempt(n, m):
    # create a set for n
    # create a set for m
    # at each iteration, compare sets for an intersection
    # return the first case of an intersection
    n_set, m_set = set(), set() 
    i = 1
    while True:
        n_set.add(n * i)
        m_set.add(m * i)
        
        res = n_set.intersection(m_set)
        if res: 
            print(i, n_set, m_set)
            return min(res)

        i += 1

def gcd(a, b):
    """
    How the GCD Implementation Works

    The gcd(a, b) function implements the Euclidean algorithm, one of the oldest 
    and most efficient ways to find the greatest common divisor of two numbers. 

    The key insight is: If a and b are two positive integers, 
    then gcd(a, b) = gcd(b, a % b)

    This works because:

    If a number d divides both a and b, then d also divides (a % b)
    If d divides both b and (a % b), then d also divides a

    """
    while b:  # Continue until b becomes 0
        # print(a, b)
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    The LCM implementation leverages a fundamental relationship between GCD and LCM:

    For any two positive integers n and m, there is a beautiful mathematical identity:

        LCM(n, m) × GCD(n, m) = n × m

    This means we can compute the LCM if we already know the GCD:

        LCM(n, m) = (n × m) ÷ GCD(n, m)

    Why This Works

    To understand why this relationship holds:

    Let's denote the prime factorizations:

    n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ
    m = p₁^b₁ × p₂^b₂ × ... × pₖ^bₖ

    The GCD takes the minimum exponent of each prime factor:

    GCD(n, m) = p₁^min(a₁,b₁) × p₂^min(a₂,b₂) × ... × pₖ^min(aₖ,bₖ)

    The LCM takes the maximum exponent of each prime factor:

    LCM(n, m) = p₁^max(a₁,b₁) × p₂^max(a₂,b₂) × ... × pₖ^max(aₖ,bₖ)

    For each prime factor pᵢ:

    min(aᵢ,bᵢ) + max(aᵢ,bᵢ) = aᵢ + bᵢ

    Therefore:

    GCD(n, m) × LCM(n, m) = n × m
    """
    return a * b // gcd(a, b)


print(lcm(4, 10))
print(lcm(5, 43))
print(lcm(73, 94))
print(gcd(4, 10))
