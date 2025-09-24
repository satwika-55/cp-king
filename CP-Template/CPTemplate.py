# ███████╗ █████╗ ████████╗██╗    ██╗██╗██╗  ██╗ █████╗ 
# ██╔════╝██╔══██╗╚══██╔══╝██║    ██║██║██║ ██╔╝██╔══██╗
# ███████╗███████║   ██║   ██║ █╗ ██║██║█████╔╝ ███████║
# ╚════██║██╔══██║   ██║   ██║███╗██║██║██╔═██╗ ██╔══██║
# ███████║██║  ██║   ██║   ╚███╔███╔╝██║██║  ██╗██║  ██║
# ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                            
 
# JAI MAHAKAAL
# jay shree radhe krishna
 
import os
import sys
import time
import random
import re
import math
import threading
import bisect
 
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
 
from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, permutations
from heapq import heapify, heappop, heappush, nlargest, nsmallest
from copy import deepcopy
from functools import cmp_to_key, lru_cache, reduce
from math import gcd,ceil,sqrt
 
# gives list of primes upto 'limit' numbers -- TC : O(Log Log N)
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return is_prime
 
def fac(n):
    factorials = [1] * (n + 1) 
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i 
    return factorials
 
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Constants
MOD1 = int(1e9 + 7)
MOD2 = 998244353
INF = int(1e17)
inf = float('inf')
 
# Alphabet and Vowel Lists
alphabets = list("abcdefghijklmnopqrstuvwxyz")
vowels = list("aeiou")
 
# Input Functions
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))
