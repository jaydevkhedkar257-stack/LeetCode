class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visitSet = set()
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        

        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for i in preMap[crs]:
                if not dfs(i): return False
            visitSet.remove(crs)

            preMap[crs] = []
            return True
        
        for i in prerequisites:
            if not dfs(i[0]):
                return False
        return True