import cProfile


def quadrados():
    return [i**2 for i in range(10_000_000)]

def cubos():
    return [i**3 for i in range(10_000_000)]

def main():
    quadrados()
    cubos()

cProfile.run('main()')