i = int(input())
arr = [0]
memo = [0] * (i+1)
for _ in range(0, i) :
  arr.append(int(input()))

memo[1] = arr[1]
memo[2] = memo[1] + arr[2]
for i in range(3, len(memo)):
  memo[i] = max(arr[i] + memo[i-2] , arr[i] + memo[i-3] + arr[i-1])

print(memo.pop())