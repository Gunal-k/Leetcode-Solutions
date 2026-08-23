class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
     if (deck.length == 0) {
            return false;
        }
        
        Map<Integer, Integer> counts = new HashMap<>();
        for (int card : deck) {
            counts.put(card, counts.getOrDefault(card, 0) + 1);
        }
        
        int gcdValue = 0;
        for (int count : counts.values()) {
            gcdValue = gcd(gcdValue, count);
        }
        
        return gcdValue >= 2;
    }
    
    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
