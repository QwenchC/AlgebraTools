import math
from functools import reduce

def gcd(a, b):
    """计算两个数的最大公因数"""
    return math.gcd(int(a), int(b))

def gcd_multiple_numbers(numbers):
    """计算多个数的最大公因数"""
    return reduce(gcd, numbers)

def lcm(a, b):
    """计算两个数的最小公倍数"""
    return abs(a * b) // gcd(a, b)

def lcm_multiple_numbers(numbers):
    """计算多个数的最小公倍数"""
    return reduce(lcm, numbers)
