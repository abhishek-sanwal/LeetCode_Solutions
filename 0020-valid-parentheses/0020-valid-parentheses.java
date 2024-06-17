class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack<>();
        
        Map<Character,Character> map = new HashMap<>(3);
        
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');
        
        for(char ch : s.toCharArray()){
            if(ch== '(' || ch =='[' || ch =='{') stack.add(ch);
            else if( !stack.isEmpty() && stack.peek() == map.get(ch)) 
                stack.pop();
            
            else
                return false;
            
        }
    
        return stack.empty();
    }
}