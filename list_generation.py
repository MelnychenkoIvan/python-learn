from timeit import Timer


def generator1(n):
    l = []
    for i in range(n):
        l = l + [i]

    return l


def generator2(n):
    l = []
    for i in range(n):
        l.append(i)

    return l


def generator3(n):
    return [i for i in range(n)]


def generator4(n):
    return list(range(n))


t1 = Timer('generator1(1000)', 'from __main__ import generator1')
print('concat ', t1.timeit(number=1000), ' millisecond')

t2 = Timer('generator2(1000)', 'from __main__ import generator2')
print('append ', t2.timeit(number=1000), ' millisecond')

t3 = Timer('generator3(1000)', 'from __main__ import generator3')
print('comprehension ', t3.timeit(number=1000), ' millisecond')

t4 = Timer('generator4(1000)', 'from __main__ import generator4')
print('list range ', t4.timeit(number=1000), ' millisecond')