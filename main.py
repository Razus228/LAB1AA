from timeit import default_timer as timer
from matplotlib import pyplot as plt
import prettytable as pt


# fibonacci number using iteration
def fibIterat(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# fibonacci number using optimization
def fibOptim(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


# fibonacci number using dynamic programming
def fibDy(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


# fibonacci number using fast doubling
def fibDouble(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib = [fib[1], fib[0] + fib[1]]
        return fib[1]


# fibonacci number using golden ratio (Binet's formula)
def fibGold(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        golden_ratio = (1 + 5 ** 0.5) / 2
        return round((golden_ratio ** n - (1 - golden_ratio) ** n) / 5 ** 0.5)


# fibonacci number using matrix multiplication
def fibM(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [[1, 1], [1, 0]]
        for i in range(2, n + 1):
            fib = [[fib[0][0] + fib[0][1], fib[0][0]], [fib[0][0], 0]]
        return fib[0][0]


# ----------------------------------------------------------------------------------
def time_complexity1():
    time1 = []
    for i in range(40):
        start = timer()
        fibIterat(i)
        end = timer()
        time1.append((end - start) * 1000)
    return time1


def time_complexity2():
    time2 = []
    for i in range(40):
        start = timer()
        fibOptim(i)
        end = timer()
        time2.append((end - start) * 1000)
    return time2


def time_complexity3():
    time3 = []
    for i in range(40):
        start = timer()
        fibDy(i)
        end = timer()
        time3.append((end - start) * 1000)
    return time3


def time_complexity4():
    time4 = []
    for i in range(40):
        start = timer()
        fibDouble(i)
        end = timer()
        time4.append((end - start) * 1000)
    return time4


def time_complexity5():
    time5 = []
    for i in range(40):
        start = timer()
        fibGold(i)
        end = timer()
        time5.append((end - start) * 1000)
    return time5


def time_complexity6():
    time6 = []
    for i in range(40):
        start = timer()
        fibM(i)
        end = timer()
        time6.append((end - start) * 1000)
    return time6


# ----------------------------------------------------------------------------------
# display the time complexity in a table
table = pt.PrettyTable()
table.field_names = ['n', 'Ration', 'Matrix', 'Double', 'Dynamic', 'Iteration', 'Optim']
for i in range(40):
    table.add_row([i, time_complexity1()[i], time_complexity2()[i], time_complexity3()[i], time_complexity4()[i],
                   time_complexity5()[i], time_complexity6()[i]])
print(table)

# display the time complexity of each algorithm in a graph
dev_x = [i for i in range(40)]
plt.xlabel('n')
plt.ylabel('Time Complexity, ms')
dev_y = time_complexity5()
plt.plot(dev_x, dev_y, label='Ratio')
dev_y = time_complexity6()
plt.plot(dev_x, dev_y, label='Matrix')
dev_y = time_complexity4()
plt.plot(dev_x, dev_y, label='Double')
dev_y = time_complexity3()
plt.plot(dev_x, dev_y, label='Dynamic')
dev_y = time_complexity1()
plt.plot(dev_x, dev_y, label='Iteration')
dev_y = time_complexity2()
plt.plot(dev_x, dev_y, label='Optim')
plt.legend()
plt.show()