import sys

def solve_2(filename):
    with open(filename, 'r') as f:
        w, n = map(int, f.readline().rstrip().split(' '))
        values, weights = zip(*[map(int, line.rstrip().split(' ')) for line in f])
    def helper(memo, size, i):
        if size == 0 or i == 0:
            return 0
        if (size, i) in memo:
            return(memo[(size, i)])
        if size < weights[i-1]:
            t = helper(memo, size, i-1)
        else:
            t = max( helper(memo, size, i-1), 
				     helper(memo, size-weights[i-1], i-1) + values[i-1] )
        memo[(size, i)] = t
        return t

    memo = {}
    return helper(memo, w, n)

	
sys.setrecursionlimit(10000)
print(solve_2('knapsack2.txt'))

	
