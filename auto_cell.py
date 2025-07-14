import copy
import operator

class CellSheet:
    def __init__(self, width, height, sheet):
        self.width = width
        self.height = height
        self.sheet = sheet
        self.rules = []

    def __str__(self):
        final_array = ""
        for y in range(self.height):
            for x in range(self.width):
                final_array += str(self.sheet[y][x]) + " "
            final_array += "\n"
        return final_array
    

    def surround(self, x, y, symbol):
        surrounding = []

        for dr in [-1, 0, 1]: 
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = y + dr, x + dc
                if 0 <= r < self.height and 0 <= c < self.width:
                    surrounding.append(self.sheet[r][c])

        return surrounding.count(symbol)


    def add(self, symbol, rule, result):
        self.rules.append([symbol, rule, result])


    def eval(self):
        temp = copy.deepcopy(self.sheet)

        for y in range(self.height):
            for x in range(self.width):
                for rule in self.rules:
                    token = temp[y][x]
                    if rule[0] == token:
                        cond = rule[1].split()
                        match cond[0]:
                            case "surround":
                                if get_truth(self.surround(x, y, cond[1]), cond[2], int(cond[3])):
                                    temp[y][x] = rule[2]

        return temp

    def step(self, times = 1):
        for _ in range(times):
            self.sheet = self.eval()

def get_truth(a, relate, b):
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '==': operator.eq}
    return ops[relate](a, b)
