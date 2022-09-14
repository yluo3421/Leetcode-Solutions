class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # thoughts
        # go through all row and col in thr 
        # use a dict to store each courses array of preq
        # use dfs to loop through all courses
        # if the course is in visited, meaning a self loop, return False
        # if the course has no preq, meaning we can always take it, return True
        # neither of the above matches,
        # add the current course to visited
        # go through the dict[current_course], which is the array of preq
        # if one of dfs(preq) return False, meaning this course cannot be taken
        # otherwise return True
        
        # example 1
        # numCourses = 2, preq = [[1,0]]
        # dict = {1: 0}
        # for course in range(numCourses):
        # we did this if statement because, when one course return True
        # it doesnt mean we can reach the end
        # but if all courses return True, meaning we can reach the end
        #   if not dfs(course):
        #       return False
        # return True
        
        prerequisitesMap = {i: [] for i in range(numCourses)}
        
        for course, preq in prerequisites:
            prerequisitesMap[course].append(preq)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            if prerequisitesMap[course] == []:
                return True
            visited.add(course)
            for preq in prerequisitesMap[course]:
                if not dfs(preq):
                    return False
            visited.remove(course)
            prerequisitesMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            