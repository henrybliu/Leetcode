class Solution:
    '''
    We can use a hashmap to store the mapping of a roman numeral to its
    integer value. When looping through, there are two cases to consider:

    Case 1:
    There needs to be some subtraction operation. This happens when the current
    number is smaller than the next one.

    Case 2:
    There doesn't need to be any subtraction. This is because the current value
    is greater than the next one.

    Time: O(n)
    Space: O(n)
    '''
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        i = 0
        res = 0
        while i < len(s):
            if i+1 < len(s) and mapping[s[i]] < mapping[s[i+1]]:
                res += mapping[s[i+1]] - mapping[s[i]]
                i+=2
            else:
                res += mapping[s[i]]
                i+=1

        return res