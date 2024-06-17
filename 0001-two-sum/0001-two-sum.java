class Solution {
    public int[] twoSum(int[] nums, int target) {
     
        int res[] = new int[2];
        
        HashMap<Integer,Integer> mapp = new HashMap<Integer, Integer>();
        
        for(int i=0;i<nums.length;++i){
            
            int req = target - nums[i];
            
            if(mapp.containsKey(req)) 
            {
                res[0] = mapp.get(req);
                res[1] = i;
                break;
            }
            mapp.put(nums[i],i);
            
        }
    
        return res;
        
           
    }
}