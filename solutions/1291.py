class Solution:
    """
    We observe that the largest number that can be created is 123456789
    becuase the largest number is 10^9. All the sequential numbers are then
    just some subsequence of 123456789. We can just try all of these
    subsequences that fall within the range of low and high and then sort the
    valid numbers.

    Time: O(n^2)
    Space: O(n)
    """

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # the largest number that can be created is 123456789
        numbers = "123456789"
        res = []

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                num = int(numbers[i : j + 1])
                if low <= num <= high:
                    res.append(num)
        res.sort()
        return res
