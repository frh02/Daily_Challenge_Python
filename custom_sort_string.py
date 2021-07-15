'''
order and str are strings composed of lowercase letters. In order, no letter occurs more than once.

order was sorted in some custom order previously. We want to permute the characters of str so that they match the order that order was sorted. More specifically, if x occurs before y in order, then x should occur before y in the returned string.

Return any permutation of str (as a string) that satisfies this property.
'''


class Solution:
    def customSortString(self, order: str, str: str) -> str:
        cnt = Counter(str)
        ans = []
        for c in order:
            if cnt[c] > 0:
                ans.append(cnt[c] * c)
                cnt.pop(c)
        for c, v in cnt.items():
            ans.append(v * c)
        return "".join(ans)
