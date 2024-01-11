class Submarine:
    def __init__(self, matrix_size):
        self.matrix_size = matrix_size
        # Extract individual dimensions
        rows, columns = self.matrix_size
        self.position_history = [[-1] * columns for _ in range(rows)]
        self.current_position = (rows // 2, columns // 2)
        self.current_depth = 0
        self.color = "yellow"
        self.valid_commands = ['forward', 'reverse', 'left', 'right', 'down', 'up']

        # Initialize starting position with depth 0
        self.update_matrix(*self.current_position, self.current_depth)

    def update_matrix(self, x, y, depth):
        self.position_history[x][y] = depth

    def process_instruction(self, instruction):
        command, value = instruction.split()
        value = int(value)

        # Update current position and depth based on the command
        if command in ['forward', 'reverse']:
            if command == 'forward':
                self.current_position = (self.current_position[0] - value, self.current_position[1])
            else:  # command == 'reverse'
                self.current_position = (self.current_position[0] + value, self.current_position[1])
        elif command in ['left', 'right']:
            if command == 'left':
                self.current_position = (self.current_position[0], self.current_position[1] - value)
            else:  # command == 'right'
                self.current_position = (self.current_position[0], self.current_position[1] + value)
        elif command == 'down':
            self.current_depth += value
        elif command == 'up':
            self.current_depth -= value
            if self.current_depth < 0:
                self.current_depth = 0
        else:
            print(f"Invalid command found: {command}")

        # Update matrix with new position and depth
        self.update_matrix(*self.current_position, self.current_depth)


class Pilot:
    def __init__(self, submarine, terrain):
        self.submarine = submarine
        self.terrain = terrain

    def navigate(self, instructions):
        for instruction in instructions:
            if self.check_collision(instruction):
                self.submarine.process_instruction(instruction)

    def check_collision(self, instruction):
        # Check collision with terrain map
        command, value = instruction.split()
        value = int(value)

        if command == 'up':
            return True  # 'up' command is always considered valid

        new_horizontal_pos = self.submarine.current_position[0]
        new_vertical_pos = self.submarine.current_position[1]
        new_depth = self.submarine.current_depth

        if command in ['forward', 'reverse']:
            if command == 'forward':
                new_horizontal_pos -= value
            else:  # command == 'reverse'
                new_horizontal_pos += value
        elif command in ['left', 'right']:
            if command == 'left':
                new_vertical_pos -= value
            else:  # command == 'right'
                new_vertical_pos += value
        elif command == 'down':
            new_depth += value
        else:
            print(f"Invalid command found: {command}")
            return False


        # Check collision with each space in the matrix being traversed
        for i in range(min(self.submarine.current_position[0], new_horizontal_pos),
                       max(self.submarine.current_position[0], new_horizontal_pos) + 1):
            for j in range(min(self.submarine.current_position[1], new_vertical_pos),
                           max(self.submarine.current_position[1], new_vertical_pos) + 1):
                if not (
                        0 <= i < self.submarine.matrix_size[0]
                        and 0 <= j < self.submarine.matrix_size[1]
                        and new_depth < self.terrain[i][j]
                ):
                    print(f"Collision with terrain! Operation rejected at grid position ({i}, {j}) terrain depth {self.terrain[i][j]}")
                    print(f"Target Position: ({new_horizontal_pos}, {new_vertical_pos}), Depth: {new_depth}")
                    print(f"Current Position: ({self.submarine.current_position[0]}, {self.submarine.current_position[1]}), Depth: {self.submarine.current_depth}")
                    return False
        return True


    def output_status(self):
        print(f"Current Position: {self.submarine.current_position}")
        print(f"Current Depth: {self.submarine.current_depth}")
        print(f"Position History:")
        for i in range(len(self.submarine.position_history)):
            print(" ".join(map(str, self.submarine.position_history[i])))


def read_terrain_from_file(filename):
    try:
        with open(filename) as fileobject:
            terrain = [list(map(int, line.strip().split())) for line in fileobject]
        return terrain
    except FileNotFoundError:
        print(f"Failed to load terrain from {filename}. File not found.")
        return None


def read_instructions(filename):
    try:
        with open(filename) as fileobject:
            instructions = [line.strip() for line in fileobject]
            return instructions
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return


def main():
    # Load instructions
    instruction_file = "submarine_kata_input_test3.txt"
    instructions = read_instructions(instruction_file)

    # Load terrain matrix from file
    terrain_filename = "terrain_matrix_1.txt"
    terrain = read_terrain_from_file(terrain_filename)
    matrix_size = (len(terrain), len(terrain[0])) if terrain else (0, 0)

    submarine = Submarine(matrix_size)
    pilot = Pilot(submarine, terrain)

    # Navigate using the pilot class
    pilot.navigate(instructions)

    # Output final position, depth, and product
    pilot.output_status()


if __name__ == "__main__":
    main()
