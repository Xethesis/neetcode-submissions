from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        num_chars_s = {}
        num_chars_t = {}

        for char in s:
            num_chars_s[char] = num_chars_s.get(char,0) + 1
        
        for char in t:
            num_chars_t[char] = num_chars_t.get(char,0) + 1
    
        return num_chars_s == num_chars_t

