import sys

t = int(sys.stdin.readline())
dp = [0] * 101

def wave():
  dp[1], dp[2], dp[3] = 1, 1, 1
  dp[4], dp[5] = 2, 2
  dp[6] = 3
  for i in range(7, 101):
    dp[i] = dp[i-1] + dp[i-5]
  return

for _ in range(t):
  n = int(input())
  wave()
  print(dp[n])
