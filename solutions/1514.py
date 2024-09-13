from collections import defaultdict, deque


class Solution:
    """
    Use Bellman Ford to update each node's greatest probability. Then return
    the end node's probability value.
    """

    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        # use Bellman Ford

        # create adjList for nodes and their edge probabilities
        adjList = defaultdict(list)
        for pair, prob in zip(edges, succProb):
            e1, e2 = pair
            adjList[e1].append((e2, prob))
            adjList[e2].append((e1, prob))

        # keep track of the greatest probabilities for each node
        probabilities = {}
        for i in range(n):
            probabilities[i] = 0
        probabilities[start_node] = 1

        # use a queue to keep looping through until no node can be further optimized
        q = deque()
        q.append(start_node)

        while q:
            curr = q.popleft()
            currProb = probabilities[curr]

            for neighbor, edgeProb in adjList[curr]:
                if probabilities[neighbor] < currProb * edgeProb:
                    q.append((neighbor))
                    probabilities[neighbor] = edgeProb * currProb

        return probabilities[end_node]
