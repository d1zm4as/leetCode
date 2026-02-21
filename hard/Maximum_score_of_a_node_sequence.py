class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node in graph:
            graph[node].sort(key=lambda x: scores[x], reverse=True)
            graph[node] = graph[node][:3]

        max_score = -1
        for u, v in edges:
            for a in graph[u]:
                if a != v:
                    for b in graph[v]:
                        if b != u and b != a:
                            max_score = max(max_score, scores[u] + scores[v] + scores[a] + scores[b])
        return max_score    