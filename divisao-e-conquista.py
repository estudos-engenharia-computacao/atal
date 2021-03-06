import statistics
import numpy as np


## Questão 1

## Resolução O(n/2) = O(n)
def mean(size, a, b):
    count = 0
    idx_ma = 0
    idx_mb = 0
    aux = []
    while count <= size:
        if a[idx_ma] <= b[idx_mb]:
            aux.append(a[idx_ma])
            idx_ma += 1
        else:
            aux.append(b[idx_mb])
            idx_mb += 1
        count += 1

    return (aux[size] + aux[size - 1]) / 2


def median_matheus(n, a1, a2):
    m1, m2 = 0, 0
    start1, start2 = 0, 0
    end1, end2 = n, n

    while True:
        if end1 - start1 <= 1 and end2 - start2 <= 1:
            break

        m1 = (start1 + end1) // 2
        m2 = (start2 + end2) // 2

        if a1[m1] == a2[m2]:
            break
        elif a1[m1] > a2[m2]:
            end1 = m1
            start2 = m2
        else:
            end2 = m2
            start1 = m1

    return (a1[m1] + a2[m2]) / 2


def median_imp(size, a, b):
    def mean_aux(ini_a, end_a, ini_b, end_b, a, b):
        ma = (ini_a + end_a) // 2
        mb = (ini_b + end_b) // 2

        if a[ma] == b[mb]:
            return (a[ma] + b[mb]) / 2
        elif end_a - ini_a <= 1 and end_b - ini_b <= 1:
            if a[ma] > b[mb]:
                return (a[end_a] + b[ini_b]) / 2
            else:
                return (a[ini_a] + b[end_b]) / 2
        elif a[ma] <= b[mb]:
            return mean_aux(ma, end_a, ini_b, mb, a, b)
        else:
            return mean_aux(ini_a, ma, mb, end_b, a, b)

    return mean_aux(0, size, 0, size, a, b)


if __name__ == '__main__':
    SIZE = 10
    for i in range(10):
        a = np.sort(np.random.randint(20, size=SIZE))
        b = np.sort(np.random.randint(20, size=SIZE))
        print(median_imp(SIZE, a, b), median_matheus(SIZE, a, b), statistics.median(a + b))
