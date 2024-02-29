# solution 1:
class Solution:
    '''
    We will traverse the input array twice going both left and right to
    calculate the produt of all of the elements to the left and then the
    right. Together, this will for the product of everything except the "self".

    Time: O(n)
    Space: O(n)
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]

        carry = 1
        for i in range(len(nums)):
            res[i] = carry
            carry *= nums[i]

        carry = 1
        for j in range(len(nums)-1, -1, -1):
            res[j]*= carry
            carry*=nums[j]

        return res
        
# solution 2:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []   
        right = []

        curr = 1
        for i in range(len(nums)):
            left.append(curr)
            curr *= nums[i]

        curr = 1
        for i in range(len(nums)-1, -1, -1):
            right.append(curr)
            curr *= nums[i]
        right = right[::-1]

        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[i])

        return res