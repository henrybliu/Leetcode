class Solution:
    '''
    Binary search on the smaller array. The "middle" indices of both arrays
    will form the median value.

    Time: O(logn)
    Space: O(1)

    where is the size of the smaller array
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1)+ len(nums2)
        #size of the left partition
        size = total//2

        #A will be the smaller array
        A = nums1
        B= nums2

        #if B is smaller, swap them
        if len(B) < len(A):
            A,B = B,A

        l = 0
        r = len(A)-1

        #a median will exist
        while True:
            Amid = l + (r-l)//2
            Bmid = size - Amid -2
            # -2 to account for 0 indexing in both arrays

            Aleft = A[Amid] if Amid >= 0 else float('-inf')
            Aright = A[Amid+1] if Amid+1 <= len(A)-1 else float('inf')
            Bleft = B[Bmid] if Bmid >=0 else float('-inf')
            Bright = B[Bmid +1] if Bmid+1 <=len(B)-1 else float('inf')

            if Aleft <= Bright and Bleft <=Aright:
                #odd
                if total %2 ==1:
                    return min(Bright, Aright)
                #even
                return (min(Aright, Bright) + max(Aleft, Bleft))/2

            #update the middle pointer
            if Aleft > Bright:
                #this means that we took too many elements in A
                r = Amid -1
            else:
                l = Amid+1