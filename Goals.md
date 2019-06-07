# Goals

## Rules of the game (**STACK**)

- Number of towers and number of discs are given
- Largest to smallest discs stacked on one tower
- Can only move one disc at a time (ex. 4,3,2,1 to 4,3,2)
- Larger discs must always be below smaller discs (ex. 5,2,1)
- *SUCCESS: All discs on* ***last*** *tower*

### Program Requirements

- Correct usage of stack .pop and .push methods (look for these methods specifically)
- Allow 3-10 discs
- **ALWAYS 3 TOWERS**
- Do not allow user to make incorrect movements (**not** only warning the user)
- Use *PyGame* interface to:
  - Display the game selection interface and rules
  - Allow for mouse control
  - Drag and drop of discs (**not click and click**)
  - Alert the user when they win
- METHODS METHODS METHODS
- \# Commenting as usual

## Layout

### Loading

- GUI intro to game with OK button
- Ask how many discs to load onto the tower [3-10]
  - Use these to load discs with values 0-9
- Load interface (3 towers/lines and 3-10 discs/flat ovals with width defined by disc values)
  - Use .push() to place onto one of 3 "tower arrays" (2D array)
  - Leave a button that allows the user to see instructions at any time
  - Attempting to quit loads a warning screen

### Gameplay

- When the user clicks and drags on a disc, attach it to the cursor
  - .pop() from the current tower stack to a temp value
- When the user releases
  - Check if in reach of a tower (defined as part of the disc touching the tower and up to a few pixels above it), otherwise .push() back onto original stack
  - If temp_value > tower_array{new}, .push() onto original stack
  - [ ] Else .push() onto new stack and release from mouse onto tower
- After each successful move, check if game is won (length of stack)
  - If so, run endgame

### Endgame

- Open an interface saying "You've won!"
- Give an option to restart the program (from the number of discs screen)

For PyGame intro, see [ThePythonGameBook](http://thepythongamebook.com/en:pygame:start) with [this site to assist](https://dr0id.bitbucket.io/legacy/pygame_tutorial00.html).
