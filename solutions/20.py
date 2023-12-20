class Solution:
    '''
    Use a stack to validate if a valid pair can be formed.

    Time: O(n)
    Space: O(n)
    '''
    def isValid(self, s: str) -> bool:
        pairs= {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if stack and c in pairs and stack[-1] == pairs[c]:
                stack.pop()
            else:
                stack.append(c)

        return len(stack)==0
