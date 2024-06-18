class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
#         difficulty = [2,4,6,8,10]
        
#         profit = [10,20,30,40,50]
        
#         worker = [4,5,6,7]
        
#         difficulty = [2,4,6]
        
#         profit = [10,20,30]
        
#         [2,10],[4,20],[6,30],[8,40],[10,50]
        
#         worker = [4,5,6,7]
        
#         30 + 30 + 20 + 20
        
#         maxmize the profit =>
        
#         each worker can do only one task
        
#         so I should assign each worker to highest profitable task acc to
#         their difficulty
        
#         profit = max(profit[i] where difficulty[i]< worker[i])
        
#         from all the tasks having difficulty less than worker[i],
#         I need to choose maximum profitable task.
        
    
#         difficulty = [2,4,6,8,10]
#         profit = [10,20,30,40,50]
        
#         worker = [4,5,6,7]
    
        arr = [[i,j] for i,j in zip(difficulty, profit)]
        # arr = [[2,10],[4,20],[6,30],[8,40],[10,50]]
        arr.sort(key=lambda x:(x[0],-x[1]))
        heap = []
        task_profit = index =  0
        worker.sort()
        max_profit = 0
        for curr_worker in worker:
            
            # Find highest profitbale task less than equal to curr_worker efficiency
            while index < len(difficulty) and arr[index][0] <= curr_worker:
                # print(arr[index],curr_worker)
                #0(logk) where k is size of heap 
                # heappush(heap,-1*arr[index][1])
                max_profit = max(max_profit, arr[index][1])
                index += 1
                
            task_profit += max_profit
#             if heap:
                
#                 #0(logk) where k is size of heap 
#                 task_profit += -1*heap[0]
                
        return task_profit
                
        
        
        
        