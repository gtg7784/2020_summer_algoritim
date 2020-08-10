import sys

def fibo(n):
  if n == 0:
    print(1,0)
  elif n == 1:
    print(0,1)
  elif n == 2:
    print(1,1)
  else:
    a=1
    b=1
    c=0
    for i in range(n-2):
      c=b
      b+=a
      a=c

    print(c, a)

z = int(sys.stdin.readline())

for i in range(z):
  x = int(sys.stdin.readline())
  fibo(x)