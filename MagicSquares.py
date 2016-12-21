#!/usr/bin/env python3

### Hyperion Development Assessment 2016
### Eynar Roshev

import magsq

def magic_square_loop() -> None:
    while True:
        query = input("\n\nPlease enter an odd natural number to create a magic square, or hit Enter to quit: ")
        if query == '':
            break
        else:
            try:
                sq = magsq.MagicSquare(int(query))
                sq.gen_magic_square()
                sq.display_magic_square()
            except:
                print("\nWrong input received. Must enter an odd natural number.")

magic_square_loop()
