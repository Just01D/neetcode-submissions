class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list= sorted(s,key = str.lower)
        t_list= sorted(t,key = str.lower)

        if s_list==t_list:
            return True
        else:
            return False