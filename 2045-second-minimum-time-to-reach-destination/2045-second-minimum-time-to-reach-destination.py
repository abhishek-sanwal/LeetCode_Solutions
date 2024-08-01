class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        
        
        INF = sys.maxsize

        source = 1

        destination = n

        adj = defaultdict(set)

        for u, v in edges:

            adj[u].add(v)
            adj[v].add(u)

        dist1 = [-1]*(n+1)
        dist2 = [-1]*(n+1)

        que = deque([[0,source]])

        while que:

            for i in range(len(que)):

                curr_weight, node = que.popleft()

                # If signal is red wait unti signal becomes green
                if (curr_weight // change)%2:

                    curr_weight = (curr_weight // change + 1)*change

                curr_weight += time

                for adjacent in adj[node]:

                    if dist1[adjacent] == -1:

                        dist1[adjacent] = curr_weight

                        que.append([curr_weight, adjacent])

                    elif dist2[adjacent] == -1 and curr_weight != dist1[adjacent]:

                        dist2[adjacent] = curr_weight
                        que.append([curr_weight, adjacent])
                        if adjacent == destination:

                            return dist2[adjacent]

        return  dist2[adjacent]






















        dist1 = [INF]*(n+1)
        dist2 = [INF]*(n+1)

        dist1[source] = 0

        min_heap = list()
        heappush(min_heap,[0, 1])

        freq = [0]*(n+1)

        while min_heap:

            curr_weight, node = heappop(min_heap)

            # If signal is red wait unti signal becomes green
            if (curr_weight // change)%2:

                curr_weight = (curr_weight // change + 1)*change

            curr_weight += time

            for adjacent in adj[node]:
                
                if freq[adjacent] == 2:
                    continue

                if curr_weight  < dist1[adjacent]:
                    
                    dist2[adjacent] = dist1[adjacent]

                    dist1[adjacent] = curr_weight

                    heappush(min_heap,[curr_weight, adjacent])

                if curr_weight < dist2[adjacent] and dist1[adjacent] != curr_weight:

                    dist2[adjacent] = curr_weight

                    heappush(min_heap,[curr_weight, adjacent])
        print(dist1,dist2)
        return dist2[n]
                


















        dist1 = [math.inf] * (n + 1)
        dist2 = [math.inf] * (n + 1)

        freq = [0] * (n + 1)
        
        min_heap = [(0, 1)]

        dist1[1] = 0
        
        while min_heap:

            curr_weight, node = heapq.heappop(min_heap)
            freq[node] += 1
            
            
            # If signal is red wait unti signal becomes green
            if (curr_weight // change)%2:

                curr_weight = (curr_weight // change + 1)*change

            curr_weight += time
            
            for neighbor in adj[node]:
                
                if freq[neighbor] == 2:
                    continue
                
                # Update distances
                if dist1[neighbor] > curr_weight:
                    
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = curr_weight
                    heapq.heappush(min_heap, (curr_weight, neighbor))
                    
                elif dist2[neighbor] > curr_weight and dist1[neighbor] != curr_weight:
                    dist2[neighbor] = curr_weight
                    heapq.heappush(min_heap, (curr_weight, neighbor))
        
        return dist2[n]
    
        # Each vertex has  weight equal to time minutes
        # Signal chnages after every change minutes

        
        
        
        
        
        
        
        
        
        
        
        
        vis = set()

        parent = [0]*(n+1)
        parent[0] = -1
        while min_heap:

            curr_weight, node = heappop(min_heap)


            if node in vis:
                continue

            vis.add(node)

            # If signal is red wait unti signal becomes green
            if (curr_weight // change)%2:

                curr_weight = (curr_weight//change + 1)*change

            for adjacent in adj[node]:
                
                total = curr_weight + time

                if total < dist[adjacent]:
                    
                    dist[adjacent] = total
                    heappush(min_heap,[total, adjacent])
                    parent[adjacent] = node

        # minimum time path is dist[n]
        
        path = list()
        node = n
        while parent[node] != -1:

            path.append(node)

            node = parent[node]

        path.reverse()
        print(path,"original")
        smallest = INF

        for i in range(len(path)-1):

            # Check if there exists a node x between path[i] and path[i+1]
            
            for node in range(0,n+1):
                
                # Via node (edges + 1)
                if node not in [path[i],path[i+1]] and node in adj[path[i]] and node in adj[path[i+1]]:
                    # print("node",node)
                    path.insert(i+1, node)
                    smallest = node
                    break

            # We have two nodes through which we can bypas this node
            # Can I skip this node ?
            if i>0 and i < len(path)-2:
            
                flag = False
                for adjacent in adj[path[i-1]]:
                    if adjacent  == path[i]:
                        continue
                    for adjacent2 in adj[adjacent]:
                        
                        for adjacent3 in adj[adjacent2]:

                            if adjacent3 == path[i+1]:

                                flag = True
                                # print("True",adjacent,adjacent2,adjacent3,path,i)
                                smallest = adjacent
                                path[i] = adjacent
                                path.insert(i+1,adjacent2)

                            if flag:
                                break
                            # print(adjacent,adjacent2,adjacent3,path[i+1],path[i-1])
                        if flag:
                            break
                    if flag:
                        break

            if smallest != INF:

                break
      
        if smallest == INF:
            # Edges + 2
            # Add first and second node as repetative
            path.insert(2,path[0])
            path.insert(3,path[1])

        print(path,"modified")

        cost = 0

        for i in range(1,len(path)):
            
            if (cost // change) % 2:
                cost = (cost//change + 1)*change
            
            cost += time
            # print(path[i],cost)
        
        # 1:[2,3]
        # 2:[1,4]
        # 3:[1,5]
        # 4:[2,5,6]
        # 5:[3,4]
        # 6:[4]

        return cost
