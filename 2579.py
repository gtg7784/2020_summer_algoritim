N = int(input())
stair_score = [int(input()) for _ in range(N)]
dp = list()

dp.append(dp[0] + stair_score[1])
dp.append(max(dp[0] + stair_score[2], stair_score[1] + stair_score[2]))

for i in range(3, N):
  dp.append(max(stair_score[i] + stair_score[i - 1] + dp[i - 3], stair_score[i] + dp[i - 2]))
print(dp[-1])