/*QUESTION:

Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
*/

#SOLUTION:
using namespace std;
class Solution {
public:
   string originalDigits(string s) {
      string nums[]= {"zero", "one", "two", "three", "four", "five", "six", "seven","eight", "nine"};
      vector <int> cnt(10);
      string ans = "";
      int n = s.size();
      for(int i = 0; i < n; i++){
         if(s[i] == 'z')cnt[0]++;
         if(s[i] == 'w') cnt[2]++;
         if(s[i] == 'g')cnt[8]++;
         if(s[i] == 'x')cnt[6]++;
         if(s[i] == 'v')cnt[5]++;
         if(s[i] == 'o')cnt[1]++;
         if(s[i] == 's')cnt[7]++;
         if(s[i] == 'f')cnt[4]++;
         if(s[i] == 'h')cnt[3]++;
         if(s[i] == 'i') cnt[9]++;
      }
      cnt[7] -= cnt[6];
      cnt[5] -= cnt[7];
      cnt[4] -= cnt[5];
      cnt[1] -= (cnt[2] + cnt[4] + cnt[0]);
      cnt[3] -= cnt[8];
      cnt[9] -= (cnt[5] + cnt[6] + cnt[8]);
      for(int i = 0; i < 10; i++){
         for(int j = 0; j < cnt[i]; j++){
            ans += (char)(i + '0');
         }
      }
      return ans;
   }
};
