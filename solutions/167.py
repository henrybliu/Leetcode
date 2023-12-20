class Solution:
    '''
    Can take advantage of the fact that it is sorted.

    Time: O(n)
    Space: O(1)
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #need to increase the indices by 1
        l = 0
        r = len(numbers)-1

        while l<r:
            add = numbers[l]+numbers[r]
            if add == target:
                return[l+1, r+1]
            elif add < target:
                l+=1
            else:
                r-=1