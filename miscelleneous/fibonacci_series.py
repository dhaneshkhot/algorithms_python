def fibonacci_series(n):
    f_series = []
    for i in range(n):
        if i == 0:
            f_series.append(0)
        elif i == 1:
            f_series.append(1)
        else:
            f_series.append(f_series[i - 1] + f_series[i - 2])
    return f_series


def fibonacci_recursive_value(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive_value(n - 1) + fibonacci_recursive_value(n - 2)


def fibonacci_series_recursive(n):
    f_series = []
    for i in range(1, n+1):
        f_series.append(fibonacci_recursive_value(i))
    return f_series
