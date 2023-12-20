class Solution:
    '''
    Convert input into lowercase letters. Test if this reads the same backwards
    and forwards.

    Time: O(n)
    Space: O(n)
    '''
    def isPalindrome(self, s: str) -> bool:
        recreate = ""
        for letter in s:
            letter = letter.lower()
            if letter.isalnum():
                recreate+=letter

        return recreate == recreate[::-1]