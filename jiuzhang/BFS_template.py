queue = collections.deque()
# if initial state has multiple nodes we put in more into dict
# distance from this node to start point
# also record if we have visited the node
distance = {node: 0} 

while queue:
    node = queue.popleft()
    for neighbor in node.neighbors():
        if neighbor in distance:
            continue
        distance[neighbor] = distance[node] + 1 # level information is the same as the distance traveled so far
        queue.append(neighbor)
