class Solution:
    '''
    Go through both halves of the string and count the number of vowels.
    Convert all letters to lowercase because the input string may consist of
    lower and uppercase letters.

    Time: O(n)
    Space: O(1)
    '''
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a','e','i','o','u'])
        firstHalf = 0
        for i in range(len(s)//2):
            if s[i].lower() in vowels:
                firstHalf +=1

        secondHalf = 0
        for i in range(len(s)-1 , (len(s)//2)-1,-1):
            if s[i].lower() in vowels:
                secondHalf +=1

        return firstHalf == secondHalf