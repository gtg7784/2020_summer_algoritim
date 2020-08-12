import sys

N,C = map(int, sys.stdin.readline().split())
home = [int(sys.stdin.readline()) for _ in range(N)]

home.sort()

def routerInstall(distance):
  count = 1
  cur_home = home[0]
  for i in range(1,N):
    if (distance <= home[i] - cur_home):
      count+=1
      cur_home = home[i]
  
  return count
            
def BinarySearch(target):
  start = 1
  end = home[-1] - home[0]

  while(start<=end):
    mid = (start+end)//2
    router_cnt = routerInstall(mid)
    if router_cnt < target:
        end = mid - 1
    elif router_cnt >= target:
        answer = mid
        start = mid + 1
  
  return answer

print(BinarySearch(C))