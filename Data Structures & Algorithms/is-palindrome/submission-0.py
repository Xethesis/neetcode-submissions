class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaner_s = []
        for char in s:
            if char.isalnum():
                cleaner_s.append(char)

        print(cleaner_s)
        print(cleaner_s[::-1])
        return cleaner_s[::-1] == cleaner_s
