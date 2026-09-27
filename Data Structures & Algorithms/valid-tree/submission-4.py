class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # trees have:
        # 1. exactly n-1 edges
        # 3. no cycles
        # 2. one connected component

        # any two conditions imply the third! so, just check first 2

        # condition 1 (simple condition)
        # condition 2 (topological sort)

        # topological sort! dfs
        # visiting, visited
        # dfs and explore a node's children
        # adj list

        # condition 1
        if len(edges) != n-1:
            return False

        adj = defaultdict(list)
        for (root, child) in edges:
            adj[root].append(child)
            adj[child].append(root)

        # condition 2
        visiting, visited = set(), set()
        def dfs(root, prev):
            # no cycle!
            if root in visited:
                return True

            # cycle!
            if root in visiting:
                return False

            visiting.add(root)
            for child in adj[root]:
                # cycle
                if child == prev:
                    continue
                if dfs(child, root) == False:
                    return False

            # no cycle!
            visiting.remove(root)
            visited.add(root)
            return True

        return dfs(0, -1) and len(visited) == n