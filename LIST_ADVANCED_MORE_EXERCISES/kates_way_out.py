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

    # Checks if Kate reached the edge of the maze and the cell is not "#' then she can escape
    if ((some_row == 0 or some_row == len(maze) - 1 or some_col == 0 or some_col == len(maze[some_row]) - 1)
            and maze[some_row][some_col] != "#"):
        return moves + 1

    maze[some_row][some_col] = "#"

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    best_moves = 0

    for d_row, d_col in directions:
        result = explore(some_row + d_row, some_col + d_col, moves + 1)
        best_moves = max(best_moves, result)

    maze[some_row][some_col] = " "

    return best_moves


rows = int(input())
maze = []
start_row = 0
start_col = 0

# maze = [
#     ["#", "k", " ", "#"],
#     ["#", " ", " ", "#"],
#     ["#", "#", "#", "#"]
# ]

# Append rows to the maze
for row in range(rows):
    current_row = list(input())
    maze.append(current_row)

for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == "k":
            start_row = row
            start_col = col

max_moves = explore(start_row, start_col, 0)

if max_moves > 0:
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")
