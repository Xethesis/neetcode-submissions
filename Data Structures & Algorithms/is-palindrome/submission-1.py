class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        print(s[::-1])
        # chars = s.split()
        s_clean =[]
        for char in s:
            if char.isalnum():
                s_clean.append(char)
        
        string = ''.join(s_clean)
        string = string.upper()

        print(string)
        print(string[::-1])
        return string == string[::-1]