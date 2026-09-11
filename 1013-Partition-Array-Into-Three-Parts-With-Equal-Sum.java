class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        int total = 0;
        for (int i : arr) {
            total += i;
        }
        if (total % 3 != 0)
            return false;
        int target = total / 3;
        int curr = 0;
        int parts = 0;
        for (int i : arr) {
            curr += i;
            if (curr == target) {
                parts += 1;
                curr = 0;
                if (parts == 3)
                    return true;
            }
        }
        return false;
    }
}
