import java.util.Objects;

class IntPair {
        
        private final int first;
        private final int second;

        public IntPair(int first, int second) {
            this.first = first;
            this.second = second;
        }

        public int getFirst() {
            return first;
        }

        public int getSecond() {
            return second;
        }

        @Override
        public boolean equals(Object o) {
            
            if (this == o) return true;
            
            if (o == null || getClass() != o.getClass()) return false;
            IntPair intPair = (IntPair) o;
            return first == intPair.first && second == intPair.second;
        }

        @Override
        public int hashCode() {
            return Objects.hash(first, second);
        }
    }
    
class Solution {

    public HashMap<IntPair,Boolean> mapp = new HashMap<>();
    
    private boolean recursion(int index, int lastJump, int[] stones){
        
        //  Base case
        if(index == stones.length-1){
            
            return true;
        }
        
        IntPair tuple = new IntPair(index,lastJump);
        
        if(mapp.containsKey(tuple))    return mapp.get(tuple);
        
        boolean flag = false;
        
        for(int i=index+1;i<stones.length;i++){
            
            if( (stones[i]- stones[index] == lastJump-1 && lastJump != 1) || stones[i] - stones[index] == lastJump|| stones[i] - stones[index] == lastJump+1 ){
                
                flag = recursion(i,stones[i]-stones[index], stones);
                if(flag) break;
                
                
            }
                
            if(stones[i]-stones[index] > lastJump+1){
                break;
            }
        }
        
        mapp.put(tuple,flag);
        
        return mapp.get(tuple);
        
    }
    
    public boolean canCross(int[] stones) {
        
        if(stones[1]-stones[0]>1){
            return false;
        }
        
        
        return recursion(1,1, stones);
                
//         private boolean function(int index =1, int last_jump =1){
            
//             // Minimum of function(k), function(k-1), function(k+1)             
            
            
            
        }
    }

//                   0
//                  /
//                 /
//                1
//              / |  \
//          (0)/  |(2) \(1)
//             1  3     X
//     }         /  \
// }         (2)/    \(3)       
//             5.     6
//        (1) / | \    \ 
//           /  |  \    \ 
//          6   X   8    8
    
    