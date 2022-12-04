class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = {}
        # d = defaultdict(dict)
        for s, e, w in roads:
            if not s in d:
                d[s] = {}
            d[s][e] = w

            if not e in d:
                d[e] = {}
            d[e][s] = w

        # It is a bfs problem
        res = inf
        dq = deque([1])
        s = set()
        s.add(1)
        
        while dq:
            node = dq.popleft()
            for e, w in d[node].items():
                if e not in s:
                    dq.append(e)
                    s.add(e)
                res = min(res, w)
                
        return res