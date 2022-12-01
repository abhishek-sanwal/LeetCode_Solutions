
def reverse(arr):
    
    start = 0
    
    end = len(arr)-1
    
    while start < end:
        
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
        

for _ in range(int(input())):
    
    n = int(input())
    
    arr = list(map(int,input().split()))
    
    reverse(arr)    
    
    print(*arr)
    

