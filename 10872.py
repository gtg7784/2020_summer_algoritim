def facto(n):
  return n * facto(n-1) if n > 1 else 1

a = int(input())
print(facto(a))