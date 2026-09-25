class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # if not prerequisites:
        #     res = [i for i in range(numCourses)]
        #     return res
        hashMap = {i:[] for i in range(numCourses)}
        visit = set()
        curr = []
        for crs, pre in prerequisites:
            hashMap[crs].append(pre)

        def dfs(crs):
            if hashMap[crs] == []:
                if crs not in curr:
                    curr.append(crs)
                return True
            if crs in visit:
                return False
            
            visit.add(crs)
            for i in hashMap[crs]:
                if not dfs(i): return False
            if crs not in curr:
                curr.append(crs)
            hashMap[crs] = []
            visit.remove(crs)

            return True

        for crs, pre in prerequisites:
            if not dfs(crs):
                return []
        
        for i in range(numCourses):
            if i not in curr:
                curr.insert(0, i)
        
            
        return curr