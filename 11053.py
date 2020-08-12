n = int(input())
answer = list(map(int, input().split()))
dp = [0] * n

for i in range(0, n):
    if i == 0 :
        dp[i] = 1
    else :
        max_dp = 0
        for j in range(0, i):
            if max_dp < dp[j] and answer[j] < answer[i]:
                max_dp = dp[j]
        dp[i] = max_dp+1

print(max(dp))