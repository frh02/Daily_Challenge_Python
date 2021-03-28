#QUESTION:
/*Palindromic Substrings
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
*/

#SOLUTION:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class Solution {
public:
    int countSubstrings(string s) {
        int count = 0;
        for(int i = 0; i < s.size(); ++i){
            count += countPalindromes(s, i, i);
            count += countPalindromes(s, i, i + 1);
        }
        return count;
    }

    // count the number of palindromes with center s[l..r]
    int countPalindromes(string &s, int l, int r){
        int count = 0;
        while(l >= 0 && r < s.size() && s[l] == s[r]){
            ++count;
            --l;
            ++r;
        }
        return count;
    }
};
