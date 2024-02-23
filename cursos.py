def ok():
    print("ok")

def canFinish(numCourses, prerequisites):
    preMap = {i:[] for i in range(numCourses)}
    for crs, pre in prerequisites:
        preMap[crs].append(pre)
        
    visitSet = set()
    def dfs(crs):
        if crs in visitSet:
            return False
        if preMap[crs] == []:
            return True
            
        visitSet.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False
        visitSet.remove(crs)
        preMap[crs] = []
        return True
            
    for crs in range(numCourses):
        if not dfs(crs): return False
    return True


'''
numCourses = 5
prerequisites = [[4,3],[3,2],[2,1],[1,0],[0,1]]
question = canFinish(numCourses, prerequisites)
if question == True:
    print("ok")
else:
    print("not ok")

'''