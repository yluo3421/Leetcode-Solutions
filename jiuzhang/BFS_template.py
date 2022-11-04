queue = collections.deque()
distance = {node: 0} # distance from this node to start point

while queue:
    node = queue.popleft()
    for neighbor in node.neighbors():
        if neighbor in distance:
            continue
        distance[neighbor] = distance[node] + 1 # level information is the same as the distance traveled so far
        queue.append(neighbor)
