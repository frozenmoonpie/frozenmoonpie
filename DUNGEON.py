MAP_FILE = 'cave_map.txt'
HELP_FILE = 'help.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    with open(map_file, 'r') as file:
        grid = [list(line.strip()) for line in file]
    return grid

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                return [i, j]

def get_command() -> str:
    """
    Gets a command from the user.
    """
    return input("Enter a command: ")

def display_map(grid, player_position):
    """
    Displays the map.
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if [i, j] == player_position:
                print('🧝', end='@')  # Player's position
            elif grid[i][j] == 'S':
                print('🏠', end='')   # Start symbol
            elif grid[i][j] == 'F':
                print('🏺', end='')   # Finish symbol
            elif grid[i][j] == '-':
                print('🧱', end='')   # Dash symbol
            elif grid[i][j] == '*':
                print('🟢', end='')   # Path symbol
        print()

def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    return [len(grid), len(grid[0])]

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    return 0 <= position[0] < grid_rows and 0 <= position[1] < grid_cols

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row, col = player_position
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('go north')
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('go south')
    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
        directions.append('go west')
    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:
        directions.append('go east')
    return directions

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    allowed_directions = look_around(grid, player_position)

    if direction.lower() in allowed_directions:
        # Create a new list for the updated player position
        new_player_position = player_position.copy()

        # Update player position based on the direction
        if direction.lower() == 'go north':
            new_player_position[0] -= 1
        elif direction.lower() == 'go south':
            new_player_position[0] += 1
        elif direction.lower() == 'go west':
            new_player_position[1] -= 1
        elif direction.lower() == 'go east':
            new_player_position[1] += 1

        # Check if the new position is inside the grid
        if is_inside_grid(grid, new_player_position):
            # Update the original player position
            player_position[:] = new_player_position
            return True
        else:
            print('Invalid move. Try again.')
    else:
        print('Invalid move. Try again.')

    return False

def check_finish(grid, player_position):
    """
    Checks if the player has reached the exit.
    """
    return grid[player_position[0]][player_position[1]] == 'F'

def display_help():
    """
    Displays a list of commands.
    """
    with open(HELP_FILE, 'r') as file:
        print(file.read())

def make_step(grid, player_position, command):
    """
    Makes a single step of the game.
    """
    directions = look_around(grid, player_position)
    if command in directions:
        direction = command.split()[1]  # Extract the actual direction after 'go'
        return move(direction, player_position, grid)
    else:
        print('Invalid move. Try again.')
        return False

def main():
    grid = load_map(MAP_FILE)
    player_position = find_start(grid)

    while True:
        display_map(grid, player_position)
        command = get_command()

        if command == 'help':
            display_help()
        elif command == 'quit':
            print('Quitting the game. Goodbye!')
            break
        else:
            success = make_step(grid, player_position, command)
            if success:
                if check_finish(grid, player_position):
                    print('Congratulations! You have reached the exit!')
                    break

if __name__ == '__main__':
    main()
