class SmallestInfiniteSet:

    def __init__(self):
        
        self.heap = []
        self.mapp = set()
        heapify(self.heap)
        self.count = 1

    def popSmallest(self) -> int:
        
        if self.heap and self.heap[0] < self.count:
        
            self.mapp.remove(self.heap[0])
            
            return heappop(self.heap)
        
        x = self.count
        
        self.count+=1
        
        return x
    
        
    def addBack(self, num: int) -> None:
        
        if self.count > num and num not in self.mapp :
            
            heappush(self.heap,num)
            self.mapp.add(num)
            
        
            
            
        
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)