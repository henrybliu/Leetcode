import math
class Solution:
    '''
    When we find a factor of n, we can use both factors that create n. We also
    notice that we only need to go up to the sqrt of n

    Time: O(logn)
    Space: O(logn)
    '''
    def kthFactor(self, n: int, k: int) -> int:
        big, small = [],[]

        for f in range(1, int(math.sqrt(n))+1):
            if n % f == 0:
                factor1 = f
                factor2 = n//f

                if factor1 == factor2:
                    small.append(factor1)
                else:
                    small.append(min(factor1,factor2))
                    big.append(max(factor1,factor2))

        together = small + big[::-1]
        
        if len(together) < k:
            return -1
        return together[k-1]