![Intro: the gelato case at opening time, pans in flavour colours, a spatula standing in the pistachio pan, mist on the marble](intro-banner.png)


# Python-Shape-Generator

![Banner](banner.png)

![Scene: the case from the front, lids opening in rotation, a spatula crossing the pistachio pan, a shape assembling row by row in a cleared tray](scene.svg)

Run `python3 python-shape-gen.py`, pick one of the five shapes by its
exact name (Square, Rectangle, Lower Left Triangle, Upper Left Triangle,
Diamond), then give it a size. Rectangle asks for a width and a height;
the others ask for one side length or radius.

The script opens with `Welcome to the shape maker!` and prints its list
with brackets and quotes, just as Python prints a list:

```
['Square', 'Rectangle', 'Lower Left Triangle', 'Upper Left Triangle', 'Diamond']
```

> **Tasting note, propped against the glass:** the exact name warning. Type one of the five names exactly, capitals and spaces included. A name that is not on the list earns the reply below, word for word, and another try.

```
Invalid choice please enter correctly
```


![Separator](sep-heavy.svg)

## The five pans, in list order

### Square

One prompt, Side length. Rows of the at sign, as many across as down:

```
@@@
@@@
@@@
```

### Rectangle

Two prompts, Width then Height, the only shape that asks two questions. An earlier version picked the height at random; the current script asks for both numbers, because a rectangle needs both:

```
@@@@
@@@@
```

![Separator](sep-light.svg)

### Lower Left Triangle

One prompt, Side length. Rows growing by one mark each time, starting from a single at sign:

```
@
@@
@@@
@@@@
```

### Upper Left Triangle

One prompt, Side length. The same row count shrinking instead, full width first, one mark last:

```
@@@@
@@@
@@
@
```

![Separator](sep-heavy.svg)

### Diamond

One prompt, Radius. The only shape drawn in hash marks instead of at signs, and the only one announced before it appears:

```
Creating Diamond
  #
 ###
#####
 ###
  #
```

Each row holds an odd count of marks, one, three, five, and the spaces in front do the centering. The widest row prints once.


![Separator](sep-light.svg)

## Sizes and refusals

Sizes are read by `read_size()`, which asks again instead of failing:

> **Tasting note:** the two size refusal messages, quoted word for word. A size typed as letters or as a fraction earns `Please enter a whole number.`. Zero or below earns `Please enter 1 or more.`.

Closing the input at any prompt ends the program quietly, with no error shown. If the width of a Rectangle comes back as a quit, the script stops there and does not ask for a height.

## Importing the draw functions

Each shape has its own draw function, and all of the asking happens in `main()` and in `read_size()`, so the file can be imported and a draw function called on its own, for instance `draw_diamond(3)`, without the welcome text and prompts getting in the way. Importing the file runs nothing.

## Files

- `python-shape-gen.py`: the whole program.
- `logo.png`, `banner.png`, `intro-banner.png`: generated branding for this repo.
- `LICENSE`: license file.
