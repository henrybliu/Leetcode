class Solution:
    '''
    Use prefix sum to store the number of zeros to the left of the current
    index. Use prefix sum to store the number of ones on the right of the
    current index. Then use both prefix sums to calculate the number of zeros
    to the left and number of ones to the right of each index and return the
    maximum.
    
    Time: O(n)
    Space: O(n)
    '''
    def maxScore(self, s: str) -> int:
        res = 0
        numZeros = [0 for _ in range(len(s))]
        numOnes = [0 for _ in range(len(s))]

        zeroCnt = 0
        for i in range(len(s)):
            if s[i] == '0':
                zeroCnt +=1
            numZeros[i] = zeroCnt

        oneCnt = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                oneCnt +=1
            numOnes[i] = oneCnt

        for i in range(len(numZeros)-1):
            res = max(res, numZeros[i] + numOnes[i+1])

        return res