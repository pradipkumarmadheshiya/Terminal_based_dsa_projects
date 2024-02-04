# Import necessary modules and classes
from pyamaze import maze, agent, textLabel
from queue import PriorityQueue

# Define a heuristic function for A* algorithm
def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

# A* pathfinding algorithm implementation
def aStar(m):
    # Define the starting cell as the bottom-right corner of the maze
    start = (m.rows, m.cols)

    # Initialize g_score and f_score dictionaries for each cell in the maze
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = h(start, (1, 1))

    # Initialize a priority queue for open cells with the initial state
    open = PriorityQueue()
    open.put((h(start, (1, 1)), h(start, (1, 1)), start))

    # Initialize a dictionary to store the parent-child relationship for the path
    aPath = {}

    # Main A* loop
    while not open.empty():
        # Get the cell with the lowest f_score from the priority queue
        currCell = open.get()[2]

        # Check if the goal is reached
        if currCell == (1, 1):
            break

        # Explore neighbors in the order of East, South, West, North
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                # Determine the coordinates of the neighbor based on the direction
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                # Calculate temporary g_score and f_score for the neighbor
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, (1, 1))

                # Update g_score, f_score, and add the neighbor to the priority queue
                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, h(childCell, (1, 1)), childCell))
                    aPath[childCell] = currCell

    # Reconstruct the forward path from the goal to the start
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    return fwdPath

# Create a maze with 12 rows and 22 columns
m = maze(12, 22)
# Generate a random maze
m.CreateMaze()

# Find the A* path in the maze
path = aStar(m)

# Create an agent in the maze with footprints enabled
a = agent(m, footprints=True)

# Trace the A* path in the maze
m.tracePath({a: path})

# Display the A* path length as a text label
l = textLabel(m, 'A Star Path Length', len(path) + 1)

# Run the maze simulation
m.run()