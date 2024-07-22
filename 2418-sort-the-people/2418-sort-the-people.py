class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        return [name for height,name in sorted(zip(heights,names),reverse=True)]
        # return [names[index] for height,index in sorted([[heights[i],i] for i in range(len(heights))],reverse=True)]
        
        # ans = list()

        # for height,index in sorted([[heights[i],i] for i in range(len(heights))],reverse=True):

        #     ans.append(names[index])

        # return ans

        MAXI =  10**5 + 1

        freq = [-1]*MAXI

        for index, height in enumerate(heights):
            freq[height] = index

        ans = list()

        for i in range(MAXI-1,-1,-1):

            if freq[i] != -1:
                ans.append(names[freq[i]])

        return ans