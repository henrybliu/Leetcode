import random

class RandomizedSet:
    '''
    A set() doesn't allow for random removal. We can instead use a random
    number generator to remove a random value from an array

    We can use a hashmap to keep track of the values that we have already
    added. An array can then hold each of the values that we currently have.
    The catch is that when removing, we need to remove the value specified and
    then fill in that cell with the end element to decrease the size of the
    array.

    Time: O(1)
    Space: O(n)

    '''    
    def __init__(self):
        self.map = {}
        self.nums = []
        
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        valIdx = self.map[val]
        lastNum = self.nums[-1]

        #update nums by removing the last element
        self.nums[valIdx] = lastNum

        #update the index of the last val in the hashmap
        self.map[lastNum] = valIdx

        # remove the val from both data structures
        self.nums.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()