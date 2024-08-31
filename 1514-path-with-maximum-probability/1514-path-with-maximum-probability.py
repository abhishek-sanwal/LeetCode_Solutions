class Solution:

    def longestPath(self, n, adj, succProb, start_node, end_node):
        
        dist = [0.0]*n

        heap = [ [-1, start_node] ]

        dist[start_node] = 1
        check = set()

        while heap:

            curr_distance, node = heappop(heap)
            curr_distance *= -1

            if node in check:

                continue

            check.add(node)

            for adjacent_node, weight in adj[node]:
                
                total_distance = curr_distance * weight

                if total_distance > dist[adjacent_node]:
                    dist[adjacent_node] = total_distance
                    heappush(heap,[-total_distance, adjacent_node])

        return dist[end_node]

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = defaultdict(list)

        for [u,v],w in zip(edges,succProb):

            adj[u].append([v,w])
            adj[v].append([u,w])

        return self.longestPath(n, adj, succProb, start_node, end_node)