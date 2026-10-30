# I wrote this to draw one of five ASCII shapes at a size the user picks.
#
# I keep each draw function separate. Each one takes a size as an argument
# and only prints its own shape. I keep all input in main() and in
# read_size(), so I can import this file and call draw_diamond(3) on its
# own without the welcome text and prompts getting in the way.

# I match these names exactly in main(). The check is a plain "in" test,
# so the spelling and capitals here are the contract. If I rename a shape
# in this list, I have to rename it in the branch below too, or that shape
# becomes impossible to pick.
CHOICES = ["Square", "Rectangle", "Lower Left Triangle",
           "Upper Left Triangle", "Diamond"]


def read_size(prompt):
    """Ask until the user gives a positive whole number, or quits.

    The first version of this script fed input() straight into int(), so a
    typo (or closing the input) ended the program with a traceback. A size
    prompt is exactly where a first-time user types the wrong thing, so it
    is the one place worth being patient.
    """
    # I use None as my quit signal. Every caller has to check for it
    # before it draws. If a caller passed None into a draw function, the
    # range() call would fail, and that failure would hide the real cause.
    while True:
        try:
            raw = input(prompt)
        except EOFError:
            # I print an empty line here so the shell prompt starts on a
            # clean line after the user closes the input.
            print()
            return None
        try:
            value = int(raw)
        except ValueError:
            # I ask again instead of failing. Text like "abc" or "3.5"
            # lands here. I treat both the same, because neither one can
            # size a shape.
            print("Please enter a whole number.")
            continue
        if value < 1:
            # I reject 0 and negative sizes here. A size of 0 would draw
            # nothing and look like a silent failure, so I say so and ask
            # again instead.
            print("Please enter 1 or more.")
            continue
        return value


def draw_square(size):
    # I build each row as one string. I use the same size for the row
    # count and for the row width, so the two cannot drift apart. A square
    # that came out taller than it is wide would be a bug here, not a
    # different shape.
    for _ in range(size):
        print("@" * size)


def draw_rectangle(width, height):
    # My first version asked for one "side length" and then picked the
    # height with random.randint(1, 10). The shape on screen had little to
    # do with what the user typed. I do not do that now. I ask for both
    # numbers, because a rectangle needs both, and a random height made
    # the result impossible to predict or test.
    for _ in range(height):
        print("@" * width)


def draw_lower_left_triangle(size):
    # I count rows from 0, so row r carries r + 1 marks. The first row is
    # a single mark, not an empty line. My first loop used the row count
    # on its own here. That shifted every row down by one and started the
    # triangle with a blank row, even though my old comment claimed the
    # opposite. I trust the count now, not the comment.
    for row in range(size):
        print("@" * (row + 1))


def draw_upper_left_triangle(size):
    # I draw this as the mirror of the lower triangle. I start at full
    # width and take one mark off each row. I keep the same total row
    # count as the lower triangle, so the two shapes line up when I print
    # them at the same size. The last row is always a single mark.
    for row in range(size):
        print("@" * (size - row))


def draw_diamond(radius):
    # I draw the diamond in two halves that share the widest middle row.
    # I use "#" here and "@" for the other shapes on purpose. That split
    # was in my first version and I kept it, so a diamond stands out in
    # the output.
    # Each row has 2 * row + 1 marks, so every row is odd and the shape
    # stays centered. The spaces in front do the centering. If I changed
    # the mark count to an even number, the point would sit off center.
    for row in range(radius):
        print(" " * (radius - row - 1) + "#" * (2 * row + 1))
    # I start the lower half at radius - 2, not radius - 1. Radius - 1 is
    # the middle row, and the loop above already printed it. If I started
    # here at radius - 1, the widest row would print twice.
    # Edge case I checked: radius 1 makes this second range empty, and
    # the whole diamond is just the single "#" from the first loop.
    for row in range(radius - 2, -1, -1):
        print(" " * (radius - row - 1) + "#" * (2 * row + 1))


def main():
    print("Welcome to the shape maker!")
    print("Choose a type of shape from the following list: ")
    # I print the list as Python prints it, brackets and quotes included.
    # That is plain, but it shows the exact spelling I expect back, which
    # matters more here than a nicer looking menu.
    print(CHOICES)
    # I loop until the user types a name from CHOICES exactly. A close
    # spelling does not count. I would rather make the user retype it
    # than guess which shape a near miss meant.
    while True:
        try:
            shape = input("> ")
        except EOFError:
            print()
            return
        if shape in CHOICES:
            break
        print("Invalid choice please enter correctly")

    # Each branch below asks for its size only after the shape is picked.
    # I do not ask for a size up front, because the rectangle needs two
    # numbers and the diamond calls its number a radius.
    if shape == "Square":
        size = read_size("Side length:\n> ")
        if size is not None:
            draw_square(size)
    elif shape == "Rectangle":
        width = read_size("Width:\n> ")
        # I stop here if the width came back as None. I do not ask for a
        # height after the user already quit. The other branches only
        # need one check, because they only ask one question.
        if width is None:
            return
        height = read_size("Height:\n> ")
        if height is not None:
            draw_rectangle(width, height)
    elif shape == "Lower Left Triangle":
        size = read_size("Side length:\n> ")
        if size is not None:
            draw_lower_left_triangle(size)
    elif shape == "Upper Left Triangle":
        size = read_size("Side length:\n> ")
        if size is not None:
            draw_upper_left_triangle(size)
    elif shape == "Diamond":
        radius = read_size("Radius:\n> ")
        if radius is not None:
            # Only the diamond prints a line like this before it draws.
            # I left that in from my first version. It is not needed, but
            # it also does no harm, and I am not changing output here.
            print("Creating Diamond")
            draw_diamond(radius)


# I guard main() with this check so importing the file runs nothing. My
# tests rely on that. Without the guard, an import would start the prompts.
if __name__ == "__main__":
    main()
