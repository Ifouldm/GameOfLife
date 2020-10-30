import PySimpleGUI as sg


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(str(self))

    def get_neighbours(self):
        up = Cell(self.x, self.y + 1)
        down = Cell(self.x, self.y - 1)
        left = Cell(self.x - 1, self.y)
        right = Cell(self.x + 1, self.y)
        upleft = Cell(self.x - 1, self.y + 1)
        upright = Cell(self.x + 1, self.y + 1)
        downleft = Cell(self.x - 1, self.y - 1)
        downright = Cell(self.x + 1, self.y - 1)
        return [up, down, left, right, upleft, upright, downleft, downright]

    def __str__(self):
        return 'x = {}, y = {}'.format(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Game:
    MAX_WIDTH = 800
    MAX_HEIGHT = 800

    living_cells = []
    all_neighbours = {}
    generation = 1
    canvas = sg.Graph(canvas_size=(MAX_WIDTH, MAX_HEIGHT), background_color='white',
                      graph_top_right=(MAX_WIDTH, MAX_HEIGHT), graph_bottom_left=(0, 0), key='graph')
    genLabel = sg.Text('Generation {}   '.format(generation), key='gen')
    buttons = [sg.Button('Proceed'), genLabel]
    layout = [[canvas], buttons]
    window = sg.Window('Game of Life', layout)
    window.Finalize()

    def __init__(self):
        self.living_cells = [Cell(1, 6), Cell(2, 6), Cell(3, 6), Cell(3, 7), Cell(2, 8),
                             Cell(10, 10), Cell(11, 10), Cell(10, 11), Cell(11, 11)]

    def get_cell_values(self):
        self.all_neighbours.clear()
        # For all live cells
        for cell in self.living_cells:
            # For each neighbour of a living cell
            for neighbour_cell in cell.get_neighbours():
                # if it exists already in the dict of all neighbours
                if neighbour_cell in self.all_neighbours:
                    # increment the count
                    self.all_neighbours[neighbour_cell] += 1
                # if it doesn't exist in the dict of all neighbours
                else:
                    self.all_neighbours[neighbour_cell] = 1

    def start_game(self):
        # Display intial layout
        self.get_cell_values()
        self.display()
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Proceed':
                # Create new generation
                self.tick()
                # Update generation display
                self.genLabel.update(value='Generation {}'.format(self.generation))
                # Look for new neighbours
                self.get_cell_values()
                # Display to screen
                self.display()
        self.window.close()

    def tick(self):
        next_gen = []
        for cell in self.living_cells:
            num_neighbours = self.all_neighbours.get(cell)
            if num_neighbours == 2 or num_neighbours == 3:
                next_gen.append(cell)
        for cell in self.all_neighbours:
            num_neighbours = self.all_neighbours.get(cell)
            if cell not in self.living_cells and num_neighbours == 3:
                next_gen.append(cell)
        self.living_cells = next_gen
        self.generation += 1

    def display(self):
        assert (len(self.living_cells) > 0)
        self.canvas.erase()
        margin = 2

        lowx = min(cell.x for cell in self.living_cells)
        hix = max(cell.x for cell in self.living_cells)
        lowy = min(cell.y for cell in self.living_cells)
        hiy = max(cell.y for cell in self.living_cells)

        x_range = hix - lowx + 1
        y_range = hiy - lowy + 1

        print('lowx= {} highx= {} range= {}'.format(lowx, hix, x_range))
        print('lowy= {} highy= {} range= {}'.format(lowy, hiy, y_range))

        cell_size = round(min(self.MAX_WIDTH / (x_range + (margin * 2)), self.MAX_HEIGHT / (y_range + (margin * 2))))

        def draw_grid():
            # Vertical lines
            for x in range(0, self.MAX_WIDTH, cell_size):
                self.canvas.draw_line(point_from=(x, 0), point_to=(x, self.MAX_HEIGHT))
            # Horizontal lines
            for y in range(0, self.MAX_HEIGHT, cell_size):
                self.canvas.draw_line(point_from=(0, y), point_to=(self.MAX_WIDTH, y))

        def draw_cell(current_cell, color='red', value=''):
            # Relative coords
            x = (current_cell.x - lowx + margin) * cell_size
            y = (current_cell.y - lowy + margin) * cell_size
            print('x = {}, y = {}'.format(x, y))
            self.canvas.DrawRectangle(top_left=(x, y + cell_size),
                                      bottom_right=(x + cell_size, y),
                                      fill_color=color, line_color='black', line_width=2)
            # self.canvas.draw_text(location=(x + (0.5 * cell_size), y + (0.5 * cell_size)),
            #                      text=str(current_cell.x) + ',' + str(current_cell.y))
            # self.canvas.draw_text(location=(x + (0.5 * cell_size), y + (0.2 * cell_size)),
            #                      text=value)

        draw_grid()

        for cell in self.living_cells:
            draw_cell(cell)

        # Draw Cells with additional formatting
        for cell in self.all_neighbours:
            alive = True if cell in self.living_cells else False
            # draw_cell(cell, color='red' if alive else 'lightBlue', value=str(self.all_neighbours[cell]))


game = Game()
game.start_game()
