from collections import deque

class Solution:
    '''
    Approach is to backtrack across all subsequences and if the length of the
    current word being built is equal to the size of its set, test if this is
    the largest word that we can create.
    
    '''
    def maxLength(self, arr: List[str]) -> int:
        ''' 
        Using BFS

        Time: O(2^n)
        Space: O(n^2)
        '''
        res = 0  
        q = deque()
        for i in range(len(arr)):
            q.append((arr[i], i))

        while q:
            currWord, currIdx = q.popleft()

            if len(currWord) == len(set(currWord)):
                res = max(res, len(currWord))

                for i in range(currIdx, len(arr)):
                    q.append((currWord + arr[i], i))

        return res


        '''
        Using DFS

        Time: same
        Space: same
        '''
        res = [0]
        def backtrack(word, idx):
            if len(word) != len(set(word)):
                return

            res[0] = max(res[0], len(word))

            for i in range(idx, len(arr)):
                backtrack(word + arr[i], i)

        backtrack('', 0)
        return res[0]
