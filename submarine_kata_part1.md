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

```
forward 5
down 5
forward 8
up 3
down 8
forward 2
```

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

Update position and depth when reading input txt file.
Need to read 3 types of input commands (could be extended in future)
We can't have negative depth (in a submarine so cant be above the surface)
After reading all input, output horizontal position, depth and the product of the two.

First thoughts, lets handle reading input.
For updating position and depth, we could loop over this with individual functions and some variables for position and depth. But this would be harder to extend in the future.

Thinking about a class structure here, we will want a Submarine Class (to store position and depth, and mod functions), a Pilot Class (to go through directions txt file) and 

Possible extensions: 
    -   draw/graph out the route and depth as we go or at the end.
    -   adding depth/position limitations based on some terrain?
    -   scope to add back/left/right to position
    -   Store past positions and depth



class Submarine:
    __init__(self, h_pos, depth):
        self.h_pos = h_pos
        self.depth = depth
        self.color = yellow

    def update_position(forward):
        self.h_pos += forward

    def update_depth(depth):
        self.depth += depth

class Pilot:
    