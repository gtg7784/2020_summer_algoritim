import sys

a = int(sys.stdin.readline())
arr = [0 for ㅑ in range(a+1)]
arr[1] = 1

for i in range(2, a+1):
  arr[i] = arr[i-1] + arr[i-2]

print(arr[-1])