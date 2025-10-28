def print_maze(maze):  # for testing
    print("   ", end="")
    for col in range(len(maze[0])):
        print(col, end=" ")
    print()
    for row in range(len(maze)):
        print(row, end="  ")
        for col in range(len(maze[row])):
            print(maze[row][col], end=" ")
        print()


def explore(some_row, some_col, moves):  # DFS search to find the longest route kate can take using recursion obv
    # check if kate's position is outside the maze boundaries
    if some_row < 0 or some_col < 0 or some_row >= len(maze) or some_col >= len(maze[some_row]):
        return 0

    # Stop recursion if kate hits a wall "#"
    if maze[some_row][some_col] == "#":
        return 0

    maze[some_row][some_col] = "#"
    moves += 1

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    best_moves = 0

    for dr, dc in directions:
        nr, nc = some_row + dr, some_col + dc
        # If neighbor is on edge and empty, Kate can escape in next step
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
            if (nr == 0 or nr == len(maze) - 1 or nc == 0 or nc == len(maze[0]) - 1) and maze[nr][nc] == " ":
                best_moves = max(best_moves, moves + 1)
            else:
                best_moves = max(best_moves, explore(nr, nc, moves))

    maze[some_row][some_col] = " "

    return best_moves


rows = int(input())
maze = []
start_row = 0
start_col = 0

# maze =
######
##k###
## ###
##  ##
#

# Append rows to the maze
for row in range(rows):
    current_row = list(input())
    maze.append(current_row)

for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == "k":
            start_row = row
            start_col = col
            break

max_moves = explore(start_row, start_col, 0)
if start_row == 0 or start_row == rows - 1 or start_col == 0 or start_col == len(maze[0]) - 1:
    max_moves = max(max_moves, 1)

if max_moves > 0:
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")
