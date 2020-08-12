a = int(input())
b = []

c = [1, 2, 4]
for i in range(4, 11):
  c.append(sum(c[-3:]))

for i in range(a):
  b.append(int(input()))

for i in range(a):
  print(c[b[i] - 1])