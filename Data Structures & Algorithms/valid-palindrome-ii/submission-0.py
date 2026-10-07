class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
                continue
            else:
                stra=s[l+1:r+1]
                strb=s[l:r]
                return stra==stra[::-1] or strb==strb[::-1]
        return True