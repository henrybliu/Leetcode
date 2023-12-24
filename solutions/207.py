from collections import defaultdict, deque

class Solution:
    '''
    Use topological sort and start with the courses that have no prerequisites
    and see if we can take all courses.
    
    Time: O(n)
    Space: O(n)
    
    where n is the number of courses
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create an adjList of which course is a prereq for each
        adjList = defaultdict(list)
        # keep a count of the number of prereqs remaining per course
        numPre = [0 for _ in range(numCourses)]

        res = []

        for c,p in prerequisites:
            adjList[p].append(c)
            numPre[c]+=1

        # start with the prereqs and see if all other classes can be reaached
        q = deque()
        for i in range(len(numPre)):
            if numPre[i]==0:
                q.append(i)

        while q:
            curr = q.popleft()
            res.append(curr)
            
            for neighbor in adjList[curr]:
                numPre[neighbor]-=1
                if numPre[neighbor] == 0:
                    q.append(neighbor)

        # check that all courses were completed
        return True if len(res)==numCourses else False