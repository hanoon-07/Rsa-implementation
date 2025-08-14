import secrets
import miller_rabin
import egcd


def is_probably_prime(x, rounds=40):
    return miller_rabin.miller_rabin(x, rounds)


def generate_random_number(bits):
    return secrets.randbits(bits)


def generate_large_prime(bits=1024, attempts=10000):
    for _ in range(attempts):
        candidate = generate_random_number(bits)
        if is_probably_prime(candidate):
            return candidate
        

def generate_prime_factors(factor_bits=1024, min_factor_delta_bits=256, attempts=10000):
    while True:
        p = generate_large_prime(factor_bits, attempts)
        q = generate_large_prime(factor_bits, attempts)
        if abs(p - q).bit_length() >= min_factor_delta_bits:
            return p, q
        
def generate_public_exponent(p, q, attempts=1000):
    euler_totient = (p - 1) * (q - 1)

    for _ in range(attempts):
        a = generate_random_number(euler_totient.bit_length())

        if a <= 1 or a >= euler_totient:
            continue

        gcd, _, _ = egcd.egcd(a, euler_totient)
        if gcd == 1:
            return a

    raise f"Failed to generate public exponent for p={p} and q={q}. Attempted {attempts} times."


def compute_private_exponent(a, p, q):
    phi = (p - 1) * (q - 1)

    gcd, b, k= egcd.egcd(a, phi) #k is not used, but egcd gives solution a⋅x+b⋅y=gcd(a,b) along with x and y
    assert(abs(gcd) == 1) #just for safety can be removed

    if b < 0:
        return b + phi
    return b
    
        

        

