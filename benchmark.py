def benchmark(func):
    import time

    def wrapper():
        start = time.time()

        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@benchmark
def cnt():
    count_ = 0
    for i in range(100*1000*1000):
        count_ += 1
    return count_


cnt()
