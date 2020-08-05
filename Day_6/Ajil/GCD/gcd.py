def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    m = max(a,b)
    n = min(a,b)
    if m%n==0 :
        return n
    return gcd(n,m%n)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))