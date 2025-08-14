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
    
        

        

