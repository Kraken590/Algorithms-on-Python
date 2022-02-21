class Solution:
    def reverseString(self, s):

        if len(s) <= 1: return s

        lo = 0
        hi = len(s) - 1

        while lo < hi:

            tmp = s[lo]
            s[lo] = s[hi]
            s[hi] = tmp

            lo += 1
            hi -= 1
        return s


s = Solution()
print(s.reverseString(['h']))
print(s.reverseString(["h","e","l","l","o"]))
print(s.reverseString(["h","e","l","l","o","w","o","r","l","d"]))