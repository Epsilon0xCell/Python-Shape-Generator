# Shape maker: draws one of five ASCII shapes at a size the user picks.
#
# Each draw function takes the size as an argument and only prints its own
# shape. Keeping input in main() and drawing in the functions means a shape
# can be called on its own (import the file, call draw_diamond(3)) without
# the welcome text and prompts getting in the way.

CHOICES = ["Square", "Rectangle", "Lower Left Triangle",
           "Upper Left Triangle", "Diamond"]


def read_size(prompt):
    """Ask until the user gives a positive whole number, or quits.

    The first version of this script fed input() straight into int(), so a
    typo (or closing the input) ended the program with a traceback. A size
    prompt is exactly where a first-time user types the wrong thing, so it
    is the one place worth being patient.
    """
    while True:
        try:
            raw = input(prompt)
        except EOFError:
            print()
            return None
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value < 1:
            print("Please enter 1 or more.")
            continue
        return value


def draw_square(size):
    for _ in range(size):
        print("@" * size)


def draw_rectangle(width, height):
    # The original asked for one "side length" and then picked the height
    # with random.randint(1, 10), so the shape on screen had little to do
    # with what the user typed. A rectangle needs both dimensions from the
    # user; anything else is a slot machine.
    for _ in range(height):
        print("@" * width)


def draw_lower_left_triangle(size):
    # Row r carries r + 1 marks, counting from 0: the first row is a single
    # mark, not an empty line. The loop used range(row) here at first, which
    # shifted every row down by one and started the triangle blank.
    for row in range(size):
        print("@" * (row + 1))


def draw_upper_left_triangle(size):
    # Mirror of the lower triangle: start full width and take one mark off
    # each row, so the two triangles share the same total row count.
    for row in range(size):
        print("@" * (size - row))


def draw_diamond(radius):
    # Two halves share the widest middle row. The lower half counts radii
    # radius-2 down to 0 because radius-1 would print the middle row twice.
    for row in range(radius):
        print(" " * (radius - row - 1) + "#" * (2 * row + 1))
    for row in range(radius - 2, -1, -1):
        print(" " * (radius - row - 1) + "#" * (2 * row + 1))


def main():
    print("Welcome to the shape maker!")
    print("Choose a type of shape from the following list: ")
    print(CHOICES)
    while True:
        try:
            shape = input("> ")
        except EOFError:
            print()
            return
        if shape in CHOICES:
            break
        print("Invalid choice please enter correctly")

    if shape == "Square":
        size = read_size("Side length:\n> ")
        if size is not None:
            draw_square(size)
    elif shape == "Rectangle":
        width = read_size("Width:\n> ")
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
            print("Creating Diamond")
            draw_diamond(radius)


if __name__ == "__main__":
    main()
