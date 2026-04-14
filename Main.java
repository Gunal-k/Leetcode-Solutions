import java.util.*;

public class Main {
    public static int[] countSubarraysOptimized(int[] arr, int k) {
        Map<Integer, Integer> prefixSumCount = new HashMap<>();
        Map<Integer, Integer> countMap = new HashMap<>();

        int sum = 0;
        int max = 0, min = Integer.MAX_VALUE;

        prefixSumCount.put(0, -1); // Base case: prefix sum of 0 at index -1

        for (int i = 0; i < arr.length; i++) {
            sum += arr[i];

            if (prefixSumCount.containsKey(sum - k)) {
                int len = i - prefixSumCount.get(sum - k);
                max = Math.max(max, len);
                min = Math.min(min, len);
                countMap.put(len, countMap.getOrDefault(len, 0) + 1);
            }

            prefixSumCount.putIfAbsent(sum, i);
        }
        if(min == Integer.MAX_VALUE) {
            min = 0;
        }
        return new int[] { countMap.get(max), countMap.get(min) };
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5,-1, 6};
        int k =  9;
        System.out.println("Number of subarrays with sum " + k + ": " + Arrays.toString(countSubarraysOptimized(arr, k)));
    }
}
