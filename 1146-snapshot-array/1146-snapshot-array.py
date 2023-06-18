
#{snap_id : idx val}
#idx snap_id
class SnapshotArray:

    def __init__(self, length: int):
        
        self.snapp = [ {} for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        
        self.snapp[index][self.snap_id] =val
        
    def snap(self) -> int:
        
        x = self.snap_id
        self.snap_id += 1
        return x

    def get(self, index: int, snap_id: int) -> int:
        
        #print(self.snapp[index])
        lis = list(self.snapp[index].keys())
        #print(lis)
        x = bisect_right(lis,snap_id)
        #print(x)
        return self.snapp[index][lis[x-1]] if x else 0
        

