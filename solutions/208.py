class Trie:
    '''
    Use a hashmap of hashmaps to create each "level" of the trie. If the next
    level has a '*', then your current level forms a valid word.

    Time: O(n)
    Space: O(n*k)
    
    where n is the max number of letters and k is the max number of words
    '''
    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        currLevel = self.root
        for s in word:
            if s not in currLevel:
                currLevel[s] = {}
            currLevel = currLevel[s]
        currLevel['*']=""
        
    def search(self, word: str) -> bool:
        currLevel = self.root
        for s in word:
            if s not in currLevel:
                return False
            currLevel = currLevel[s]
        if '*' in currLevel:
            return True
        return False 

    def startsWith(self, prefix: str) -> bool:
        currLevel = self.root
        for s in prefix:
            if s not in currLevel:
                return False
            currLevel = currLevel[s]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)