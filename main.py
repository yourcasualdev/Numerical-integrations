import math
from numpy import linspace


# Sağdan dikdortgen
def sagdik(func, a, b, n):
    array = linspace(a, b, n)
    toplam = 0
    for i in range(n-1):
        head = array[i]
        end = array[i+1]

        toplam = toplam + (end-head)*(func(end))
    return toplam


# Soldan Dikdortgen
def soldik(func, a, b, n):
    array = linspace(a, b, n)
    toplam = 0
    for i in range(n-1):
        head = array[i]
        end = array[i+1]

        toplam = toplam + (end-head)*(func(head))
    return toplam


# Mid Point
def midpoint(func, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += func((a + h/2.0) + i*h)
    result *= h
    return result


# Yamuklar Teoremi
def yamukkurali(func, a, b, n):
    array = linspace(a, b, n)
    toplam = 0
    for i in range(n-1):
        head = array[i]
        end = array[i+1]

        toplam = toplam + (end-head)*(func(head)+func(end))/2
    return toplam


# Simpson 1/3
def simp13(func, a, b, n):

    # h Değeri bulunur.
    h = (b - a)/n

    # List for storing value of x and f(x)
    x = list()
    fx = list()

    # x ve f(x) değeri hesaplanır.
    i = 0
    while i <= n:
        x.append(a + i * h)
        fx.append(func(x[i]))
        i += 1

    res = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:
            res += fx[i]
        elif i % 2 != 0:
            res += 4 * fx[i]
        else:
            res += 2 * fx[i]
        i += 1
    res = res * (h / 3)
    return res


# Simpson 3/8
def simp38(func, lower_limit, upper_limit, interval_limit):

    interval_size = (float(upper_limit - lower_limit) / interval_limit)
    toplam = func(lower_limit) + func(upper_limit)

    # Calculates value till integral limit
    for i in range(1, interval_limit):
        if (i % 3 == 0):
            toplam = toplam + 2 * func(lower_limit + i * interval_size)
        else:
            toplam = toplam + 3 * func(lower_limit + i * interval_size)

    return ((float(3 * interval_size) / 8) * toplam)


# Weddle
def weedle(func, a, b):

    # Adım sayısını bul h
    h = (b - a) / 6

    # Toplam
    toplam = 0

    toplam = toplam + (((3 * h) / 10) * (func(a)
                                         + func(a + 2 * h)
                                         + 5 * func(a + h)
                                         + 6 * func(a + 3 * h)
                                         + func(a + 4 * h)
                                         + 5 * func(a + 5 * h)
                                         + func(a + 6 * h)))

    return toplam


# Boole
def boolerule(func, a, b):
    n = 4
    h = ((b - a) / n)
    toplam = 0

    bl = (7 * func(a) + 32 * func(a + h) + 12 *
          func(a + 2 * h)+32 * func(a + 3 * h)+7 *
          func(a + 4 * h)) * 2 * h / 45

    toplam = toplam + bl
    return toplam


def main():
    n = 30
    a = 1
    b = 3

    # Fonksiyonun Tanımı.
    def f(x): return math.exp(x)

    # Gerçek sonuç.
    real = 17.3673
    print(f'Gerçek sonuç =     {real}')
    print(f'Sağdan dikdortgen: {sagdik(f,a, b, n)}')
    print(f'Soldan dikdortgen: {soldik(f,a, b, n)}')
    print(f'midpoint         : {midpoint(f,a, b, n)}')
    print(f'Yamuklar yöntemi : {yamukkurali(f,a, b, n)}')
    print(f'Simpson 1/3      : {simp13(f,a, b, n)}')
    print(f'Simpson 3/8      : {simp38(f,a, b, n)}')
    print(f'Weddle           : {weedle(f,a, b,)}')
    print(f'Boole            : {boolerule(f,a, b)}')


if __name__ == "__main__":
    main()
