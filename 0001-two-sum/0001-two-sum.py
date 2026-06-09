class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # we have an integer target 
        # return the indices of the two numbers that add to the targert
        #brute force way would be to iterate the array add each number to the coming numbers and checkin irf they add up to the target 
         # hash map implementation 

        hmap = {} #nums = [2,7,11,15] target ==9
        for i in range(len(nums)):# iterating through the array nums 

            
            complement = target - nums[i] # complemnt we get from subtracting the target 
            if complement in hmap: # search the number in the hmap as a key 
                return [i,hmap[complement]] # returning both indices 
            hmap[nums[i]]= i # Add the number as a key and the index as a value 

            # the key of a two sum when we use the hashmap is to not store first 
            # check if it is in hahmap if not add the number as a key loacting to a index 
            #hmap[nums[i]]= i



         

    
       
            
            



        