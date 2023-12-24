class Solution:
    '''
    Perform union-find to find if a connection is unneeded. An edge will form a
    cycle if the two nodes are already connected.

    Time: O(n)
    Space: O(n)
    
    where n is the number of nodes
    '''
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # find the max number of nodes
        numNodes = 0
        for n1,n2 in edges:
            numNodes = max(numNodes, max(n1,n2))

        parent = [i for i in range(numNodes+1)]
        rank = [1 for i in range(numNodes+1)]

        def find(node):
            # we have found the parent node when we point to ourself
            while node != parent[node]:
                # path compression
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            # this is a redundant edge because these two nodes are already connected
            if p1 == p2:
                return True

            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2]+= rank[p1]
                parent[p1] = p2

            return False

        # want to return the last edge that can be removed if multiple
        res = None

        for n1, n2 in edges:
            if union(n1,n2):
                res = [n1,n2]

        return res
