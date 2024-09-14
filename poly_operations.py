import numpy as np

def poly_div(dividend, divisor):
    """多项式除法，返回商和余数"""
    dividend = np.trim_zeros(dividend, 'f')
    divisor = np.trim_zeros(divisor, 'f')
    len_diff = len(dividend) - len(divisor)
    if len_diff < 0:
        return np.array([0]), dividend
    quotient = np.zeros(len_diff + 1)
    for i in range(len_diff + 1):
        coeff = dividend[i] / divisor[0]
        quotient[i] = coeff
        subtract = coeff * np.pad(divisor, (0, len_diff - i), 'constant')
        dividend = dividend - np.pad(subtract, (i, 0), 'constant')
    remainder = np.trim_zeros(dividend, 'f')
    return quotient, remainder

def poly_gcd(a, b):
    """计算两个多项式的最大公因式"""
    a = np.trim_zeros(a, 'f')
    b = np.trim_zeros(b, 'f')
    while np.any(b):
        _, r = poly_div(a, b)
        a, b = b, r
    return a / a[0]

def gcd_multiple_polynomials(polynomials):
    """计算多个多项式的最大公因式"""
    gcd = polynomials[0]
    for poly in polynomials[1:]:
        gcd = poly_gcd(gcd, poly)
    return gcd

def poly_lcm(a, b):
    """计算两个多项式的最小公倍式"""
    gcd = poly_gcd(a, b)
    lcm = np.polymul(a, b) / gcd
    return np.trim_zeros(lcm, 'f')
