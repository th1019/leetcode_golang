import string
import math


class Solution1:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 1
        letters = list(string.ascii_letters)
        letter_prime = dict()
        letter_prime[letters.pop()] = 2
        for i in range(3, 1000, 2):
            if self.isPrime(i):
                letter_prime[letters.pop()] = i
                cnt += 1
            if cnt == 52:
                break

        product = 1

        i_start = i_end = 0
        longest_string = str()
        for i in range(len(s)):
            if letter_prime.get(s[i],None) is None:
                continue
            if product % letter_prime[s[i]] != 0:
                product *= letter_prime[s[i]]
                i_end += 1
                longest_string=s[i_start:i_end]
            else:
                if len(longest_string) <= i_end - i_start:
                    longest_string = s[i_start:i_end]
                i_start = i_end
                i_end += 1
                product = letter_prime[s[i]]

        return len(longest_string)

    def isPrime(self, i):
        if i <= 3:
            return i >= 2
        if (i % 2 == 0) | (i % 3 == 0):
            return False

        for j in range(5, math.ceil(math.sqrt(i)) + 1, 6):
            if i % j == 0 | i % (j + 2) == 0:
                return False
        return True

class Solution(object):
    def lengthOfLongestSubstring(self, s):
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
