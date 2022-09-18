def friend_distance(friends, userA, userB):
    # Your code here...
    # thoughts 
    # for each user, we can go over his list of friends and get his 
    # direction connection, record them as 1st level
    # take each friend and go to next level until we hit the userB
    if userA == userB:
        return 0
    
    level = 1
    def bfs(friends, userA, userB, level):
        
        queue = collections.deque()
        
        # could use visited to avoid duplicates
        for i in range(friends[userA]):
            if i == userB and friends[userA][i] == 1:
                return level
            elif friends[userA][i] == 1:    
                queue.append()
        while queue:
            bfs(friends, queue.popleft(), userB, level + 1)
        return -1
    return bfs(friends, userA, userB, level)