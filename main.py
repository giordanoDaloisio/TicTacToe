from Game import TicTacToeGame
import Heuristics as h
import time


def minmax(game, state, player):
    beststate = None

    if state.complete():
        return h.heuristic(state, MAX), state

    if player is MAX:
        currval = float('-inf')
        for node in game.neighbors(state, MAX):
            val, state = minmax(game, node, MIN)
            if val > currval:
                currval = val
                beststate = node

    if player is MIN:
        currval = float('inf')
        for node in game.neighbors(state, MIN):
            val, state = minmax(game, node, MAX)
            if val < currval:
                currval = val
                beststate = node
    return currval, beststate


def alpha_beta(game, state, player, alpha=float('-inf'), beta=float('inf')):
    beststate = state
    if state.complete():
        return h.heuristic(state, MAX), state
    if player is MAX:
        currval = float('-inf')
        for node in game.neighbors(state, player):
            val, state = alpha_beta(game, node, MIN, alpha, beta)
            alpha = max(alpha, val)
            if val > currval:
                currval = val
                beststate = node
            if alpha >= beta:
                break
        return currval, beststate
    if player is MIN:
        currval = float('inf')
        for node in game.neighbors(state, player):
            val, state = alpha_beta(game, node, MAX, alpha, beta)
            beta = min(beta, val)
            if val < currval:
                currval = val
                beststate = node
            if alpha >= beta:
                break
        return currval, beststate




def human_move(game, player):
    pos = ""
    while pos not in [str(i) for i in range(1, 10)]:
        pos = input("Make your move [1-9]")
    state = game.setPosition(player, pos)
    while state is None:
        print("Position not valid \n")
        pos = input("Make your move [1-9]")
        state = game.setPosition(player, pos)
    return state


def ai_vs_ai(game, player):
    global MAX
    global MIN
    MAX = "X"
    MIN = "O"
    while not game.state.complete():
        val, move = minmax(game, game.state, player)
        game.makeMove(move)
        print("Value: "+str(val))
        print(game.state)
        if player is MAX:
            player = MIN
        elif player is MIN:
            player = MAX
    if game.state.solution(MAX):
        print("MAX wins!")
    elif game.state.solution(MIN):
        print("MIN wins!")
    elif game.state.full():
        print("DRAW!")


def man_vs_ai(game):
    global MAX
    global MIN
    MAX = ""
    MIN = ""
    human_turn = ""

    while MIN not in ["X", "O"]:
        MIN = input("Choose X or O:").upper()
    if MIN == "X":
        MAX = "O"
    elif MIN == "O":
        MAX = "X"

    while human_turn not in ["y", "n"]:
        human_turn = input("Start first? [y, n]:")

    print(game.state)
    while not game.state.complete():
        if human_turn is "y":
            state = human_move(game, MIN)
            game.makeMove(state)
            human_turn = "n"
            print(game.state)
            continue
        if human_turn is "n":
            start_time = time.time()
            val, state = alpha_beta(game, game.state, MAX)
            game.makeMove(state)
            human_turn = "y"
            print("Value: "+str(val))
            print(game.state)

    if game.state.solution(MIN):
        print("You win!")
    elif game.state.solution(MAX):
        print("You lose!")
    elif game.state.full():
        print("Draw!")


game = TicTacToeGame([["-" for i in range(0, 3)] for j in range(0, 3)])
man_vs_ai(game)
