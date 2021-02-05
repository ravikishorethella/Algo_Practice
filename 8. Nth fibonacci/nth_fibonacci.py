'''
find the Nth fibonacci numbers
'''

# recursive approach
# time - O(2^n) - for each recursive call, we will be calling two more calls
# space - O(n) - n call stacks 
def getNthFib(n):
    if n == 1: 
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n - 1) + getNthFib(n - 2)

# recursive approach with memoization
# time - O(n) - for n numbers, we have to recursively call n-1, n-2 ... n-n
# space - O(n)
def getNthFib(n, memoize = {1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        return memoize[n]

# iterative approach
# time - O(n)
# space - O(1)
def getNthFib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nthFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nthFib
    return lastTwo[1] if n > 1 else lastTwo[0]