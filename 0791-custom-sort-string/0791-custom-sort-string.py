class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        mapp = {ele: i for i, ele in enumerate(order)}
        
        s = [i for i in s]
        s.sort(key= lambda x:mapp.get(x,0))
        
        return "".join(s)