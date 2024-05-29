class Solution {
    public int countSubstrings(String s) {
        int res = 0;
        int length = s.length();

        for(int i = 0; i < length; i++){
            int l = i, r = i;
            while (l >= 0 && r < length && s.charAt(l) == s.charAt(r) ){  //odd length palindrome
                res = res + 1;
                l --;
                r ++;
            }
            l = i;
            r = i + 1;
            while (l >= 0 && r < length && s.charAt(l) == s.charAt(r) ){  //even length palindrome
                res = res + 1;
                l --;
                r ++;
            }
        }
        return res;
    }
}