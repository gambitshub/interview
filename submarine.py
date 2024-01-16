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


--- Part Two ---

Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.

Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Here's a repeat of the example instructions from part 1:
```
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

With our changes to the commands, these example instructions do something different:
forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.

After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?


END OF INSTRUCTIONS

Recap:
    -   Up/down dictates orientation
        -   0 = flat
        -   Down +ve move=, orientation is down.
        -   Up -ve move, orientation higher.
    -   Forward still increases horizontal position by value & increases depth by aim multiplied by value

Recap:
    - Update position and depth when reading input txt file.
    - Need to read 3 types of input commands (could be extended in future)
    - We can't have negative depth (in a submarine so cant be above the surface)
    - After reading all input, output horizontal position, depth and the product of the two.


For updating position and depth, we could loop over this with individual functions and some variables for position and depth. But this would be harder to extend in the future.

Thinking about a class structure, we will want a Submarine Class (to store position and depth, and mod functions), a Pilot Class (to go through directions txt file). 

Possible extensions: 
    -   draw/graph out the route and depth
    -   adding depth/position limitations based on some terrain?
        - think of 2d matrix with depth values could give valid positions
    -   scope to add back/left/right to position
        - either having x&y position
        - or consider current direction of sub (heading/orientation) when moving forward
    -   add speed to distance?
    -   Store a log of past positions and depth
    -   add some input checking / exception handling
    -   add limit to the depth the submarine can go
"""


class Submarine:
    def __init__(self, horizontal_pos = 0, depth = 0, color = "yellow"):
        # init pos and depth to 0
        self.horizontal_pos = horizontal_pos
        self.aim = 0 # init to 0
        self.depth = depth
        self.color = color

    def product(self):
        return self.horizontal_pos * self.depth

    def update_position(self, command, value):
        # forward will change position and depth
        if command == 'forward':
            self.horizontal_pos += value
            self.depth += value * self.aim
            if self.depth < 0:
                self.depth = 0
        # down to change aim
        elif command == 'down':
            self.aim += value
        # up to change aim
        elif command == 'up':
            self.aim -= value
        else:
            print(f"Invalid command found: {command}")

    def output_status(self):
            print(f"Horizontal Position: {self.horizontal_pos}")
            print(f"Depth: {self.depth}")
            print(f"Product: {self.product()}")

class Pilot:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def navigate(self, instructions):
        for instruction in instructions:
            command, value = instruction.split()
            value = int(value)
            self.vehicle.update_position(command, value)

    def output_status(self):
        self.vehicle.output_status()


def read_instructions(filename):
    try:
        with open(filename) as fileobject:
            instructions = [line.strip() for line in fileobject]
            return instructions
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return


def main():
    instructions_file = "submarine_kata_input_test.txt"
    instructions = read_instructions(instructions_file)

    submarine = Submarine()
    pilot = Pilot(submarine)

    # navigate using pilot class
    pilot.navigate(instructions)

    # output final position, depth and product
    pilot.output_status()
    
    # testing first instruction
    command, value = instructions[0].split(" ")
    value = int(value)
    sub2 = Submarine()
    sub2.update_position(command, value)
    if sub2.horizontal_pos == 5:
        print(f"quick test passed")
    else:
        print(f"test failed")


if __name__ == "__main__":
    main()