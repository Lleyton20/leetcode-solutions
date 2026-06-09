class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if nums[i] + nums[j]== target:
                    return [i,j]
        # nums is an array with integers
        # we have an integer target 
        # return the indices of the two numbers that add to the targert
        #brute force way would be to iterate the array add each number to the coming numbers and checkin irf they add up to the target 
         

    
       
            
            



        