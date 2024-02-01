class Solution:
    '''
    After sorting, we can recognize that that if there is ever a difference
    greater than k between any number, then there is no arrangement that can
    yield a viable answer. So, we can greedily try to keep adding the next
    number to the current array we are trying to create. Since there are only 3
    elements total per array, we can simply use a couple of conditionals to
    check that there exists no difference in the array that is greater than k.

    Time: O(nlogn)
    Space: O(n)
    '''
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = [[] for _ in range(len(nums)//3)]

        currArr = 0
        for num in nums:
            # case when the current array being built is empty
            if not res[currArr]:
                res[currArr].append(num)
            # case when we only have one element in the current array being built
            elif len(res[currArr]) == 1 and num - res[currArr][-1] <= k:
                res[currArr].append(num)
            # case when there are two elements in the current array being built
            elif len(res[currArr])==2 and num-res[currArr][-1] <= k and num-res[currArr][-2] <= k:
                res[currArr].append(num)
            # we can't add the number to the current array
            else:
                return []

            if len(res[currArr]) == 3:
                currArr += 1

        return res