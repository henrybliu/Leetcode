from collections import defaultdict, deque

class Solution:
    '''
    Create a map of the words missing one letter and the next words that it can
    possibly be. We then use BFS to find the shortest path to reach endWord.

    Time: O(n*k)
    Space: O(n*k)

    where n is the number of words and k is the length of the longest word
    '''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mapp = defaultdict(list)

        # check if endWord is even possible
        if endWord not in wordList:
            return 0

        # map words missing one letter to all the possible words that it can next be
        for word in wordList:
            for i in range(len(word)):
                blank = word[:i] + '_' + word[i+1:]
                mapp[blank].append(word)

        # perform BFS from the beginWord to endWord to find least number of transforms
        q = deque()
        q.append(beginWord)
        used = set()
        transforms = 1

        while q:
            for i in range(len(q)):
                curr = q.popleft()
                
                if curr == endWord:
                    return transforms

                used.add(curr)
                for i in range(len(curr)):
                    blank = curr[:i] + '_' + curr[i+1:]
                    for word in mapp[blank]:
                        if word not in used:
                            q.append(word)
                            # don't want to add previously added words
                            used.add(word)

            transforms +=1 

        # it isn't possible to reach the endWord
        return 0
                