import sys
 
a = []
a.append(1)
a.append(0)
 
b = []
b.append(0)
b.append(1)
 
for i in range(40):
  a.append(a[i] + a[i+1])
  b.append(b[i] + b[i + 1])
 
T = int(sys.stdin.readline().rstrip())
 
for i in range(T):
  n = int(sys.stdin.readline().rstrip())
  print(a[n],b[n])