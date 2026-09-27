class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs on connected component
        # every dfs call --> a component
        # only call dfs on nodes that are unvisited
        # number of dfs calls --> number of connected components

        # maintain prev pointer to avoid cycles

        adj = defaultdict(list)
        for (p, q) in edges:
            adj[p].append(q)
            adj[q].append(p)

        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)
        
        numComponents = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            numComponents += 1
        return numComponents