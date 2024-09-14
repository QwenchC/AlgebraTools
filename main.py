from poly_operations import gcd_multiple_polynomials, poly_lcm
from number_operations import gcd_multiple_numbers, lcm_multiple_numbers
from prime_operations import count_primes_less_than


def input_numbers():
    """用户输入数字"""
    nums = input("请输入数字（用空格分隔）：")
    return [int(x) for x in nums.split()]


def input_polynomials():
    """用户输入多项式"""
    polynomials = []
    num_polynomials = int(input("请输入多项式的数量："))
    for i in range(num_polynomials):
        poly_str = input(f"请输入第 {i + 1} 个多项式的系数（从高次项到低次项，用空格分隔）：")
        poly = [float(x) for x in poly_str.split()]
        polynomials.append(poly)
    return polynomials


def main():
    print("选择求解工具:")
    print("1. 多项式最大公因式")
    print("2. 多项式最小公倍式")
    print("3. 数字最大公因数")
    print("4. 数字最小公倍数")
    print("5. 小于某数的素数个数")

    choice = input("请输入选择（1-5）：")

    if choice == '1':
        polynomials = input_polynomials()
        result = gcd_multiple_polynomials(polynomials)
        print("多个多项式的最大公因式为:", result)

    elif choice == '2':
        poly1 = input_polynomials()[0]
        poly2 = input_polynomials()[1]
        result = poly_lcm(poly1, poly2)
        print("两个多项式的最小公倍式为:", result)

    elif choice == '3':
        numbers = input_numbers()
        result = gcd_multiple_numbers(numbers)
        print("多个数的最大公因数为:", result)

    elif choice == '4':
        numbers = input_numbers()
        result = lcm_multiple_numbers(numbers)
        print("多个数的最小公倍数为:", result)

    elif choice == '5':
        n = int(input("请输入一个数字："))
        result = count_primes_less_than(n)
        print(f"小于 {n} 的素数个数为:", result)

    else:
        print("无效的选择，请重新运行程序并选择 1-5 之间的选项。")


if __name__ == "__main__":
    main()
