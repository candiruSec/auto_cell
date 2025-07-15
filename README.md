# auto_cell

An actually cool python "library" for creating cellular automata

## Use

Just import the lib and create a cell table with
```
cell_variable = auto_cell.CellSheet(x, y, sheet)
```
With "sheet" being a pre-created 2d array.

### Rules

Rules are made with this style:
```
cell_variable.add('A', "function B OP N", 'C')
```
Essentially the code checks when the table has symbol A, and where it does, if function(B) OP (==, >, <) N, then turn A into C.

### Functions

So far there is just "surround" which checks how many of a certain symbol surround another.
