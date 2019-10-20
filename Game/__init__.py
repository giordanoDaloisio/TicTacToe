from copy import deepcopy


class TicTacToeRepr:

    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        ris = ""
        for row in self.grid:
            ris += "| "
            for cell in row:
                ris += str(cell)+" | "
            ris += "\n"
        return ris


class TicTacToeState:

    def __init__(self, representation, parent=None):
        self.representation = representation
        self.parent = parent

    def solution(self, player):
        grid = self.representation.grid
        solutions = [
            [grid[0][0], grid[0][1], grid[0][2]],
            [grid[1][0], grid[1][1], grid[1][2]],
            [grid[2][0], grid[2][1], grid[2][2]],
            [grid[0][0], grid[1][0], grid[2][0]],
            [grid[0][1], grid[1][1], grid[2][1]],
            [grid[0][2], grid[1][2], grid[2][2]],
            [grid[0][0], grid[1][1], grid[2][2]],
            [grid[0][2], grid[1][1], grid[2][0]]
        ]
        if [player, player, player] in solutions:
            return True
        return False

    def full(self):
        for row in self.representation.grid:
            if 0 in row:
                return False
        return True

    def complete(self):
        return self.solution("X") or self.solution("O") or self.full()

    def __str__(self):
        return str(self.representation)


class TicTacToeGame:

    def __init__(self, grid):
        self.state = TicTacToeState(TicTacToeRepr(grid))

    def neighbors(self, state, player):
        repr = state.representation
        out = set([])
        for i in range(0, len(repr.grid)):
            for j in range(0, len(repr.grid[i])):
                if repr.grid[i][j] == 0:
                    new_grid = deepcopy(repr.grid)
                    new_grid[i][j] = player
                    new_state = TicTacToeState(TicTacToeRepr(new_grid), self.state)
                    out.add(new_state)
        return out

    def makeMove(self, state):
        self.state = state

    def setPosition(self, player, pos):
        repr = self.state.representation
        position_dict ={
            "1": (0, 0),
            "2": (0, 1),
            "3": (0, 2),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "7": (2, 0),
            "8": (2, 1),
            "9": (2, 2)
        }
        x, y = position_dict[pos]
        if repr.grid[x][y] == 0:
            new_grid = deepcopy(repr.grid)
            new_grid[x][y] = player
            return TicTacToeState(TicTacToeRepr(new_grid), self.state)
        return None

