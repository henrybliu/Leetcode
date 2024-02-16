from collections import Counter

class Solution:
    '''
    We can use bucket sort where the indices are the frequencies and the values
    the number of integers at that frequency. We then realize that the values
    of the array are the unique number of elements. We can remove these
    occurrences in two cases: 

    - case 1 - k is greater than the number integers times the frequency
        - k can remove all occurrences 

    - case 2 - k cannot remove all occurrences
        - k can only remove k // frequency of the number of integers

    Time: O(n)
    Space: O(n)
    '''
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # cell in buckets means that there are buckets[i] values with frequency
        # i
        buckets = [0 for _ in range(len(arr)+1)]
        counts = Counter(arr)

        for f in counts.values():
            buckets[f]+=1

        res = len(counts)
        for f in range(1, len(buckets)):
            intWithFreq = buckets[f] # number of ints with f frequency
            # case were we remove the entire bucket
            if k >= f * intWithFreq:
                k -= f * intWithFreq
                 # decrement by number of unique elements that can be removed
                res -= intWithFreq
            else: # k could only remove some of the elements
                canRemove = k//f
                res -= canRemove
                break

        return res

