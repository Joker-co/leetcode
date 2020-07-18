# BFS 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        adj = [[] for i in range(numCourses)]

        for cur, pre in prerequisites:
            indegree[cur] += 1
            adj[pre].append(cur)
        
        num_res = numCourses
        q = []
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        while len(q):
            flag = q[0]
            del(q[0])
            num_res -= 1
            for i in adj[flag]:
                indegree[i] -= 1
                if indegree[i]==0:
                    q.append(i)
        return num_res==0

# DFS
def moni(cur, adj, flags):
    if flags[cur]==-1:
        return True
    if flags[cur]==1:
        return False
    flags[cur] = 1
    
    for i in adj[cur]:
        if not moni(i, adj, flags):
            return False
    flags[cur] = -1
    return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        flags = [0]*numCourses
        adj = [[] for i in range(numCourses)]

        for cur, pre in prerequisites:
            adj[cur].append(pre)
        
        for i in range(numCourses):
            if not moni(i, adj, flags):
                return False
        return True
