class Solution:
    '''
    Use backtracking to generate all valid parentheses strings. We know whether
    to add a "(" or ")" depending on the count of each so far.

    Time: O(n^2)
    Space: O(n^2)
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        stack = []
        
        def backtrack(opened, closed):
            if opened == closed == n:
                parentheses.append("".join(stack))
                return
            
            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closed)
                stack.pop()
                
            if closed < opened:
                stack.append(")")
                backtrack(opened, closed + 1)
                stack.pop()
                
        backtrack(0,0)
        return parentheses