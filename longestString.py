import string

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # initial parameters
        location = dict()
        letters = list(string.ascii_letters)
        i_start =0

        if len(s) == 0:
            return 0
        l_string=s[0]
        for i in range(len(s)):
            if s[i] not in letters:
                continue
            if location.get(s[i], None) is not None:
                if i_start <= location.get(s[i]):
                    i_start = location[s[i]]+1
            #print(f"i={i},i_start={i_start},{l_string},{location}")
            if (i-i_start+1) > len(l_string):
                l_string = s[i_start:i+1]
            location[s[i]] = i
        return len(l_string)



if __name__=="__main__":
    a=Solution()
    s = ["a","ac","dvdf","abcabcbb","pwwkew","abba"]
    for i in s:
        l=a.lengthOfLongestSubstring(i)
        print(i,l)
