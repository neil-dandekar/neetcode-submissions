class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = {char: [] for word in words for char in word}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            l = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:l] == w2[:l]:
                return ""
            for j in range(l):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break
        
        visiting = set()
        visited = set()

        order = []
        def dfs(u):
            if u in visited:
                return False

            if u in visiting:
                return True

            visiting.add(u)
            for v in adj[u]:
                if dfs(v):
                    return True
            visiting.remove(u)

            visited.add(u)
            order.append(u)

        for u in adj:
            if dfs(u):
                return ""

        order.reverse()
        return ''.join(order)
