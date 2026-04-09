class Solution {
    public boolean haveConflict(String[] event1, String[] event2) {
        int s1 = convertToMinutes(Integer.parseInt(event1[0].split(":")[0]),Integer.parseInt(event1[0].split(":")[1]));
        int e1 = convertToMinutes(Integer.parseInt(event1[1].split(":")[0]),Integer.parseInt(event1[1].split(":")[1]));
        int s2 = convertToMinutes(Integer.parseInt(event2[0].split(":")[0]),Integer.parseInt(event2[0].split(":")[1]));
        int e2 = convertToMinutes(Integer.parseInt(event2[1].split(":")[0]),Integer.parseInt(event2[1].split(":")[1]));
        return s1 <= e2 && s2 <= e1;
        // return event1[0].compareTo(event2[1]) <= 0 &&
        //        event2[0].compareTo(event1[1]) <= 0;
    }
    private int convertToMinutes(int h, int m){
        return (h * 60) + m;
    }
}