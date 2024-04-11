class Solution:
    """
    We are not able to convert strings to integers directly (type casting or a
    hashmap). A workaround is to use the ASCII values of a string to recreate
    the number as an int. Then, we can multiply this out as normal before
    converting the product back to a string. We can once again use its ASCII
    value to convert it back to a string.


    Time: O(n)
    Space: O(m)

    where n is the longer of num1 or num2 and m is the number of digits in the product
    """

    def multiply(self, num1: str, num2: str) -> str:
        # convert the string to a num using ord -- the ASCII value differences from 0
        def stringToNum(num):
            res = 0
            for i in range(len(num)):
                res += (ord(num[i]) - ord("0")) * (10 ** (len(num) - 1 - i))
            return res

        def numToString(num):
            # edge case where the product is 0
            if not num:
                return "0"

            res = ""

            while num:
                toAdd = num % 10
                num = num // 10

                toAdd = chr(toAdd + ord("0"))

                # creating the product string from right to left
                res = toAdd + res

            return res

        num1 = stringToNum(num1)
        num2 = stringToNum(num2)
        product = num1 * num2
        return numToString(product)
