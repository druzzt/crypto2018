import sys
import math
from fractions import gcd
seedGlobal = 1234567        # the "seed"
m = 695042276722573170      # the "multiplier"
c = 9490547368738284388     # the "increment"
n = 4775783922337203685     # the "modulus"

class prng_lcg:
    def __init__(self, seed):
        self.state = seed

    def next(self):
        self.state = (self.state * m + c) % n
        return self.state
    
def test():
    gen = prng_lcg(seedGlobal)
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next()
    print gen.next() 

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n
    else:
        return 0

def unk_inc(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def unk_mul(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return unk_inc(states, modulus, multiplier)

def unk_mod(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return unk_mul(states, modulus)

def test1():
    gen = prng_lcg(seedGlobal)
    arr = []
    for i in range(6):
        arr.append(gen.next())
    print arr
    mod, mul, inc = unk_mod(arr)
    print mod, mul, inc
    return mod, mul, inc

def predict(mod, mul, inc):
    return (seedGlobal * mul + inc) % mod

mod, mul, inc = test1()
nextPredicted = predict(mod, mul, inc)
test()
print "Predicted:", nextPredicted

