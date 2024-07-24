class Solution:
    """
    Map each digit to its mapping value. Sort the nums array values by its
    associated mapped value. This solution could be optimized by using math to
    retrieve each number's digits.
    """

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mappedVals = {}
        for num in nums:
            strNum = str(num)
            mappedVal = ""
            for digit in strNum:
                digit = int(digit)
                mappedVal += str(mapping[digit])

            mappedVals[num] = int(mappedVal)

        numsWithMappedVals = [(num, mappedVals[num]) for num in nums]
        numsWithMappedVals.sort(key=lambda numWithMappedVal: numWithMappedVal[1])
        return [numWithMappedVal[0] for numWithMappedVal in numsWithMappedVals]
