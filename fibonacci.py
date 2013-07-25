__author__ = 'Daan Debie'

# O(c^n)
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# O(n)
def fib_iterator():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


# Remembers calculated values
def fib_memoization(n, memo=dict()):
    if n < 0:
        return 'Negative n not allowed.'
    elif n == 0 or n == 1:
        return n
    else:
        if n not in memo:
            memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
        return memo[n]

print "recursive"
print fib_recursive(6)
print "iterator"
n = 1
for i in fib_iterator():
    if n > 7:
        break
    print i
    n += 1
print "memoization"
print fib_memoization(6)

