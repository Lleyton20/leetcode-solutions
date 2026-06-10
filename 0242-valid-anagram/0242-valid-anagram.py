class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        if len(s)!= len(t):
            return False
        for char in s :
            count[ord(char)-ord('a')] +=1

        for char in t :
            count[ord(char)-ord('a')] -=1

        for nums in count: # checking if all the characters have the same result 
            if nums !=0:
                return False
            

        return True
        

    

    