import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = "".join([char for char in s if char.isalnum()])

        start = 0
        end = len(cleaned_s)-1

        while start <= end:
            if cleaned_s[start].lower() != cleaned_s[end].lower():
                return False
            
            start+=1
            end-=1

        return True