class Solution:
    '''
    We can add the special cases into the numbers we check if it can divide
    into nums. We then try to divide nums by largest numbers possible.

    Example:
    2994 : 2994 // 1000 = 2 --> we can fit 2 1000s
        2994 % 2000 = 994

    994 : 994 // 900 = 2 --> we can fit 1 900
        994 % 900 = 94

    94 : 94 // 90 = 1 --> we can fit 1 90
        94 % 90 = 4

    4 : 4 // 4 = 1 --> we can fit 1 4
        4 % 4 = 0

    Time : O(1)
    Space: O(n)

    where n is the number of digits needed in the result
    '''
    def intToRoman(self, num: int) -> str:
        bases = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        mapping = {
            1 : 'I',
            5 : 'V',
            10 : 'X',
            50 : 'L',
            100 : 'C',
            500 : 'D',
            1000 : 'M',
            4 : 'IV', # minus 1
            9 : 'IX',
            40 : 'XL',
            90 : 'XC',
            400 : 'CD',
            900 : 'CM'       
        }

        res = ""
        # want to try to divide by the largest number possible
        for base in bases:
            factor = num // base
            if factor >= 1:
                # how many of base can we fit into num?
                res += factor * mapping[base]
                # update the num
                num %= base
            
        return res