class Solution:
    """
    We can use a custom compare function. For example, given the numbers 3 and
    34, we want to check whether 334 or 343 is larger. Since 343 is larger, we
    want to prioritize 34. We can do this with a custom comparator. So the
    sorted array should be [34, 3] in decreasing order.
    """

    def largestNumber(self, nums: List[int]) -> str:
        stringNums = [str(num) for num in nums]

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                # 1 means that n1 is greater
                return 1
            else:
                # -1 means that n1 is less
                return -1

        # use python's custom compare function
        stringNums.sort(key=cmp_to_key(compare), reverse=True)

        # convert to int and then back into a string to get rid of leading zeros
        return str(int("".join(stringNums)))
