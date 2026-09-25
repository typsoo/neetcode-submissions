class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph =[[] for _ in range(n)]
        visited = [False for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(u):
            visited[u] = True

            for neighbour in graph[u]:
                if not visited[neighbour]:
                    dfs(neighbour)

        cnt = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                cnt +=1

        return cnt