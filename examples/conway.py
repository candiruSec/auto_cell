import auto_cell
import time
import os
import random

def main():
    sheet = [ ['.'] * 30 for _ in range(30)]

    for i in range(200):
        sheet[random.randint(0, 29)][random.randint(0, 29)] = 'X'

    t = auto_cell.CellSheet(30, 30, sheet)
    
    t.add('.', "surround X == 4", 'X')
    t.add('X', "surround X < 2", '.')
    t.add('X', "surround X > 3", '.')

    while True:
        os.system("clear")
        print(t)
        t.step()
        time.sleep(0.1)


if __name__ == "__main__":
    main()
