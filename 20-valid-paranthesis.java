class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character,Character> map = Map.of(')','(','}','{',']','[');
        for(int i=0;i<s.length();i++){
            Character val = s.charAt(i);
            if(map.containsKey(val)){
                if(!stack.isEmpty() && stack.peek() == map.get(val)){
                    stack.pop();
                }
                else return false;
            }
            else stack.push(val);
        }
        return stack.isEmpty() ? true : false;
    }
}