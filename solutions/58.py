class Solution:
    '''
    Start at the back of the string s and create the last word. Remove extra
    white space as needed.

    Time: O(n)
    Space: O(n)
    '''
    def lengthOfLastWord(self, s: str) -> int:
        string_index = len(s)-1
        letter_counter = 0

        while s[string_index] == ' ':
            string_index-=1

        while s[string_index] != ' ' and string_index>=0:
            letter_counter+=1
            string_index-=1
        return letter_counter

