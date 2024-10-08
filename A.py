import heapq

class Node:
    def __init__(self, position, parent= None, g=0, h= 0):
        self.position = position
        self.parent = parent
        self.g = g 
        self.h = h 
        self.f = g + h 

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] + goal[1])

def astar(grid, start, goal):
    open_list = []
    closed_list = set()
    
    start_node = Node(position= start, g=0, h=heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == goal:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        neighbors = [(0,1), (1,0), (0,-1), (-1,0)]
        for move in neighbors:
            neighbor_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            if (0 <= neighbor_position[0] < len(grid)) and (0 <= neighbor_position[1] < len(grid[0])):
                if grid[neighbor_position[0]][neighbor_position[1]] == 1:
                    continue
                if neighbor_position in closed_list:
                    continue

            g = current_node.g + 1
            h = heuristic(neighbor_position, goal)
            neighbor_node = Node(position=neighbor_position, parent=current_node, g=g, h=h)

            heapq.heappush(open_list, neighbor_node)

    return None

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)  # Điểm bắt đầu
goal = (4, 4)   # Điểm đích

path = astar(grid, start, goal)
if path:
    print("Đường đi tìm được:", path)
else:
    print("Không tìm được đường đi")

