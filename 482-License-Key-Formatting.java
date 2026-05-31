class Solution {
    public String licenseKeyFormatting(String s, int k) {
        String ms = s.replace("-","").toUpperCase();
        int i = ms.length() % k;
        if(i == 0) i = k;
        int j = 0;
        List<String> ans = new ArrayList<>();
        while(i<=ms.length()){
            ans.add(ms.substring(j,i));
            j = i;
            i += k;
        }
        return String.join("-",ans);
    }
}