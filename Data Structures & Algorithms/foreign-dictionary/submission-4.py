from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        # create edges
        edges = defaultdict(list)
        for w in words:
            for c in w:
                edges[c]
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            j = 0

            end = min(len(w1), len(w2))
            while j < end and w1[j] == w2[j]:
                j += 1

            if j < end:
                edges[w1[j]].append(w2[j])
            elif len(w1) > len(w2):
                return ""

        # top sort
        ordering = []
        visited = set()
        visiting = set()
        def dfs(u): # returns whether cycle is found
            if u in visited:
                return False
            if u in visiting:
                return True

            visiting.add(u)
            for v in edges.get(u, []):
                if dfs(v):
                    return True
            visiting.remove(u)
            
            visited.add(u)
            ordering.append(u)
            return False

        for u in edges:
            if dfs(u):
                return ""

        ordering.reverse()
        # print(ordering)
        return "".join(ordering)