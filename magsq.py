#!/usr/bin/env python3

### Hyperion Development Assessment 2016
### Eynar Roshev

### Contains a class that represents the odd magic square
### and operations for working on it, e.g its generation

class MagicSquare:
    def __init__(self, n: int) -> None:
        "Initialise a magic square. Input n must be an odd natural number"

        if (n % 2) != 0 and n > 0:
            self.n = n
            self.magic_constant = (n * (n**2 + 1)) // 2
        else:
            raise Exception("Expected an odd number, but got {}".format(n))

    def gen_magic_square(self) -> None:
        "Generates an odd nxn magic square"

        if self.n == 1:
            self.cells = ([1],)
            return

        cells = tuple([0 for x in range(self.n)] for x in range(self.n))
        max_cells = self.n * self.n

        row = 0
        column = self.n // 2
        cells[row][column] = 1

        for i in range(2, max_cells+1):
            initial_row = row
            initial_column = column

            if row == 0: # uppermost row
                row = self.n-1 # wrap around to last row
            else:
                row -= 1

            if column == self.n-1:
                column = 0
            else:
                column += 1

            while cells[row][column]: # a number exists at that position
                if row == self.n-1:
                    row = 0
                else:
                    row = initial_row+1
                column = initial_column

            cells[row][column] = i

        self.cells = cells

    def display_magic_square(self) -> None:
        "Prints out the magic square to the screen"

        print("Magic square of order {}x{}. All rows and columns add up to {}.\n".format(self.n, self.n, self.magic_constant))
        for row in self.cells:
            srow = "\t".join([str(x) for x in row])
            srow = "\t{}".format(srow)
            print(srow)
