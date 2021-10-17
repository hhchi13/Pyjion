def test_floats(n=10000):
    for y in range(n):
        x = 0.1
        z = y * y + x - y
        x *= z


def test_ints(n=10000):
    for y in range(n):
        x = 2
        z = y * y + x - y
        x *= z


def test_bigints(n=10000):
    for _ in range(n):
        x = 200_100_100_100_100_100_100_100_100
        y = 100_100_100_100_100_100_100_100_100
        z = y * y + x - y
        x *= z


def test_function_calls(n=10000):
    def f():
        pass
    for _ in range(n):
        f()


__benchmarks__ = [
    (test_floats, "floatmath_micro", {"level": 2}),
    (test_ints, "intmath_micro", {"level": 2, "pgc": True}),
    (test_bigints, "bigintmath_micro", {"level": 2, "pgc": True}),
    (test_function_calls, "function_call_micro", {"level": 2, "pgc": True})]