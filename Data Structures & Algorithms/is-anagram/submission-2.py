from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        num_chars_s = defaultdict(int)
        num_chars_t = defaultdict(int)

        for char in s:
            num_chars_s[char] += 1
        
        for char in t:
            num_chars_t[char] +=1
    
        return num_chars_s == num_chars_t

