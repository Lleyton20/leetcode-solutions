class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #output is an arrray containin the indices of the two numbers that add up to a target
        #input is an array of integers 
        # nums = [3,2,4] (3+2) (3+4) (2+4) (4+2)
        #DO WE ASSUME THAT THE NUMBERS THE ARRAY ARE SORTED 
        #OPTIMISED BY A TWO POINTER ALGORITHM 
        left = 0  # start the first position elementt of the pointer
        right = len(numbers)-1 # the last position element of the array 

        while left < right:
            sum_nums = numbers[left] + numbers[right]
            if sum_nums < target:
                left+=1

            elif sum_nums >target:
                right-=1

            else:
                return [left+1,right+1]

            pass
