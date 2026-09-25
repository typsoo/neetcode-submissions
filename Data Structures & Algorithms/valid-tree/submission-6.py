class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph =[[] for _ in range(n)]
        visited = [False for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(u, prev):
            visited[u] = True

            a = True
            for neighbour in graph[u]:
                if not visited[neighbour] and dfs(neighbour, u):
                    a = True

                elif neighbour != prev:
                    return False

            return a


        if not dfs(0, None): return False

        
        return all(v == True for v in visited) 
