a = input()

for i in range(1, int(a) + 1):
  if i == int(a):
    print('*'*(2*i-1))
  elif i == 1:
    print(' '*(int(a)-i),'*',sep='')
  else:
    print(' '* (int(a)-i),'*',' '*(2*i-3),'*', sep='')