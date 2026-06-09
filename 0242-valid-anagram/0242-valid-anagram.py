from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case anagrams have the same number of letters thus same len 
        # we could sort the strings and if they equal to each other we can we return true 
        if len(s) != len(t):
            return False

        s= Counter(s)
        t= Counter(t)
        return s == t
      

   

        

    

    