
#{snap_id : idx val}
#idx snap_id
class SnapshotArray:

    def __init__(self, length: int):
        
        self.snapp = [ {} for i in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        
        self.snapp[index][self.snap_id] = val
        
    def snap(self) -> int:
        
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        
        lis = list(self.snapp[index].keys())
        
        x = bisect_right(lis,snap_id)
        return self.snapp[index][lis[x-1]] if x else 0
        

