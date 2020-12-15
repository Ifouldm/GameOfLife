# GameOfLife
Conway's Game of Life: [Game of Life - Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

The classic Conway's game of life in Python, this is a test project using 2D drawing, canvas', cartesian coordinates, arrays. Given an initial state of "living" cells the grid propagates with each generation based on a set of rules described in the wikipedia article above.The challenge on this project is down to the unlimited scope, theoretically the game is of infinite dimensions and also continues infinitely.

- [x] Define 2D array of cells
- [x] Initialise starting criteria
- [x] Display grid
- [x] Display living cells
    - [x] Display neighbour cells (useful for debugging)
- [x] Caclulate next generation
- [x] Increment generations manually (button)
- [x] Display generation number
- [x] Zoom out to display all living cells
- [ ] Increment generations automatically (timer)

### Additional goals

- [ ] Allow input to change initial living cells
- [ ] Allow input to toggle cells while running

## Dependencies

- [PySimpleGUI](https://pysimplegui.readthedocs.io/)

## Images

![Conway's Game of Life](https://i.imgur.com/F4LTKRA.png "Conway's Game of Life Image")

## Run Application

```sh
python3 game.py
```
