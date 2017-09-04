with open('Knapsack1.txt', 'r') as f:
    w, n = [int(x) for x in f.readline().rstrip().split(' ')]
    values, weights = zip(*[map(int, line.rstrip().split(' ')) for line in f])


dp = [[0] * (w+1) for _ in range(n+1)]

for i in range(1, n+1):
    for k in range(0, w+1):
        if k < weights[i-1]:
            dp[i][k] = dp[i-1][k]
        else:
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-weights[i-1]] + values[i-1])

print(dp[n][w])

