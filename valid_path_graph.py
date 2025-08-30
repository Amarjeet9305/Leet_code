# Write a program to find valid path in graph as per given source and destination.

class Solution:
    def validPath(self, n, edges, source, destination):
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append[v]
            graph[v].append[u]  # Because undirected
        # Define DFS(Breadth first search)
        visited = set()
        queue = deque([source])
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False
# Driver Code

sol = Solution()
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
print(sol.validPath())               
            