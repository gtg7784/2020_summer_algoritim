def hanoi(n, frm, to, ohter):   
  if n < 2: 
    print(frm, to)
    return
  hanoi(n-1, frm, ohter, to)
  print(frm, to)
  hanoi(n-1, ohter, to, frm)

n = int(input())
print((2**n)-1)
hanoi(n, 1, 3, 2)