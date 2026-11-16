class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
        s_clean = ''.join(cleaned)
        s_rev = s_clean[::-1]
        return s_clean == s_rev
