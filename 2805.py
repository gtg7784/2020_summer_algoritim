N, M = map(int, input().split()) 
trees = list(map(int, input().split())) 

def solve(): 
  lowest, highest = 0, max(trees)
  
  while lowest != highest:
    middle = (lowest + highest + 1)//2
    bring = sum([(h - middle if h > middle else 0) for h in trees])
    if bring >= M:
      lowest = middle
    else:
      highest = middle - 1 
    
  return highest
    
print(str(solve()))
