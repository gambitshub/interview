"""
--- Submarine Puzzle ---
Bam! You've found yourself teleported in a submarine, deep under the sea.
Now, you need to figure out how to pilot this thing.
It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:
    forward X increases the horizontal position by X units.
    down X increases the depth by X units.
    up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.
The "down" command will _increase_ your depth, and the up command _decreases_ it.
The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

Your horizontal position and depth both start at 0. The steps above would then modify them as follows:
```
    forward 5 adds 5 to your horizontal position, a total of 5.
    down 5 adds 5 to your depth, resulting in a value of 5.
    forward 8 adds 8 to your horizontal position, a total of 13.
    up 3 decreases your depth by 3, resulting in a value of 2.
    down 8 adds 8 to your depth, resulting in a value of 10.
    forward 2 adds 2 to your horizontal position, a total of 15.
```

After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

END OF INSTRUCTIONS

Recap:
    - Update position and depth when reading input txt file.
    - Need to read 3 types of input commands (could be extended in future)
    - We can't have negative depth (in a submarine so cant be above the surface)
    - After reading all input, output horizontal position, depth and the product of the two.


For updating position and depth, we could loop over this with individual functions and some variables for position and depth. But this would be harder to extend in the future.

Thinking about a class structure, we will want a Submarine Class (to store position and depth, and mod functions), a Pilot Class (to go through directions txt file) and 

Possible extensions: 
    -   draw/graph out the route and depth as we go or at the end. using matplotlib
    -   adding depth/position limitations based on some terrain?
        - think of 2d matrix with depth values could give valid positions
    -   scope to add back/left/right to position
        - either having x&y position
        - or consider current direction of sub (heading) when moving forward
    -   Store a log of past positions and depth
"""

import matplotlib.pyplot as plt
from PIL import Image  # Import Image from Pillow

class Submarine:
    def __init__(self):
        self.horizontal_pos = 0 # init to 0
        self.depth = 0 # init to 0
        self.color = "yellow"

    def update_horizontal_position(self, forward_change):
        self.horizontal_pos += forward_change

    def update_depth(self, depth_change):
        self.depth += depth_change
        # check if depth value is negative (i.e. above sea level)
        if self.depth < 0:
            self.depth = 0

    def get_position(self):
        return self.horizontal_pos, self.depth


class Pilot:
    def __init__(self, submarine):
        self.submarine = submarine

    def navigate(self, instructions):
        for instruction in instructions:
            command, value = instruction.split()
            value = int(value)
            if command == 'forward':
                self.submarine.update_horizontal_position(value)
            elif command == 'down':
                self.submarine.update_depth(value)
            elif command == 'up':
                self.submarine.update_depth(-value)

    def output_status(self):
        print(f"Horizontal Position: {self.submarine.horizontal_pos}")
        print(f"Depth: {self.submarine.depth}")
        print(f"Product: {self.submarine.horizontal_pos * self.submarine.depth}")

    def plot_route(self, instructions):
        positions = [self.submarine.get_position()]
        for instruction in instructions:
            command, value = instruction.split()
            value = int(value)
            if command == 'forward':
                self.submarine.update_horizontal_position(value)
            elif command == 'down':
                self.submarine.update_depth(value)
            elif command == 'up':
                self.submarine.update_depth(-value)
            positions.append(self.submarine.get_position())

        horizontal_positions, depths = zip(*positions)

        plt.plot(horizontal_positions, depths, marker='o')
        plt.xlabel('Horizontal Position')
        plt.ylabel('Depth')
        plt.title('Submarine Route and Depth')
        plt.show()


def main():
    try:
        # open input file
        with open("submarine_kata_input.txt") as fileobject:
            # print(fileobject.readlines()) # check input
            instructions = [line.strip() for line in fileobject]
    except FileNotFoundError:
        print("File not found. Please make sure the input file exists.")
        return

    submarine = Submarine()
    pilot = Pilot(submarine)

    # navigate using pilot class
    pilot.navigate(instructions)

    # output final position, depth and product
    pilot.output_status()        

    # plot submarine route
    pilot.plot_route(instructions)


if __name__ == "__main__":
    main()