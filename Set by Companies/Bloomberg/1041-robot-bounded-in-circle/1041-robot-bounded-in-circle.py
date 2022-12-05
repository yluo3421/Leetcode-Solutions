class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        We need to find a way to determine if there is a loop
        during the instructions.
        Maybe that after enough cycles, there is the same amount of
        west == east, north == south, meaning there is a cycle
        
        ////It's a limit cycle trajectory if the robot is back to the center: x = y = 0 or if the robot doesn't face north: idx != 0.
        proof lets say after one cycle robot facing k and k != 0
        after 4 cycles, the direction is (k * 4) % 4 = 0
        lets say start with (x, y), and one cycle it becomes 
        (x + dx, y + dy)
        after one cycle, facing north:
        x_4_cycles = x + dx + dx + dx + dx = x + 4 * dx
        y_4_cycles = y + dy + dy + dy + dy= y + 4 * dy
        
        after one cycle, fcaing east
        x_4_cycles = x + dx + dy - dx - dy = x
        y_4_cycles = y + dy - dx - dy + dx= y
        
        after one cycle facing south
        x_4_cycles = x + dx - dx + dx - dx = x
        y_4_cycles = y + dy - dy + dy - dy= y
        
        after one cycle facing west
        x_4_cycles = x + dx - dy - dx + dy = x
        y_4_cycles = y + dy + dx - dy - dx = y
        """
        # north, east, south, west
        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        
        x, y = 0, 0
        dir_idx = 0
        
        for i in instructions:
            if i == "L":
                dir_idx = (dir_idx + 3) % 4
            elif i == "R":
                dir_idx = (dir_idx + 1) % 4
            else:
                x += directions[dir_idx][0]
                y += directions[dir_idx][-1]
        return (x == 0 and y == 0) or dir_idx != 0
         