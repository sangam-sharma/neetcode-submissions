class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sexy=set()
        res=0
        l=0
        for i in range(len(s)):
            while s[i] in sexy:
                sexy.remove(s[l])
                l+=1
            sexy.add(s[i])
            res=max(res,i-l+1)
        return res

