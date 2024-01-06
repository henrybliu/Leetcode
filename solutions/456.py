class Solution:
    '''
    Use a stack to maintain the the '1' and '3' of the pattern that we have
    encountered so far. Use a monotonic increasing stack to maintain that the
    largest value seen so far must be greater than num.

    Time: O(n)
    Space: O(n)
    '''
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # (currMin is smallest seen so far, number where number > currMin, )
        currMin = float('inf')

        for num in nums:
            while stack and stack[-1][1] <= num:
                stack.pop()

            if stack and stack[-1][1] > num and stack[-1][0] < num:
                return True

            stack.append((currMin, num))
            currMin = min(currMin, num)

        

        return False
        



        


    
