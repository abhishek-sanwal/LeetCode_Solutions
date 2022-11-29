# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        arr = list()
        
        def tree(root):
            
            if not root:
                
                return 
            
            tree(root.left)
            arr.append(root.val)
            tree(root.right)
            
        ans = []
        tree(root)
        print(arr)
        def bs(arr,val):
            
            start = 0
            end = len(arr) - 1
            
            while start <= end:
                
                mid = ( start + end) //2
                
                if arr[mid] == val or mid <len(arr)-1 and arr[mid] <val and arr[mid+1] >val:
                    return mid
                
                elif arr[mid] > val:
                    end = mid-1
                    
                    
                else:
                    start = mid+1
                    
            return start
                
        
        for value in queries:
            
            if value < arr[0]:
                
                ans.append([-1,arr[0]])
                
            elif value > arr[-1]:
                ans.append([arr[-1],-1])
            else:
                x = bs(arr,value)
                #print(x)
                if arr[x] == value:
                    ans.append([value,value])

                else:
                    ans.append([arr[x],arr[x+1]])
                
        return ans
            
        