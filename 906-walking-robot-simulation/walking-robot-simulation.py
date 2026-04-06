class Solution(object):
    def robotSim(self, commands, obstacles):
        # Direction vectors: North, East, South, West
        # North: (0, 1), East: (1, 0), South: (0, -1), West: (-1, 0)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        # Current position and direction index (0 = North)
        x = y = di = 0
        
        # Convert obstacles to a set of tuples for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        
        max_sq_dist = 0
        
        for cmd in commands:
            if cmd == -2:  # Turn left
                di = (di - 1) % 4
            elif cmd == -1:  # Turn right
                di = (di + 1) % 4
            else:  # Move forward k units
                for _ in range(cmd):
                    next_x = x + dx[di]
                    next_y = y + dy[di]
                    
                    # Check if the next step is an obstacle
                    if (next_x, next_y) not in obstacle_set:
                        x, y = next_x, next_y
                        # Update max squared distance at each step
                        max_sq_dist = max(max_sq_dist, x*x + y*y)
                    else:
                        # Hit an obstacle, stop moving for this command
                        break
                        
        return max_sq_dist