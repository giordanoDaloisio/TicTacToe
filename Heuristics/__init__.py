def heuristic(state, player):
    if player is "X":
        if state.solution("X"):
            return 1
        if state.solution("O"):
            return -1
    if player is "O":
        if state.solution("O"):
            return 1
        if state.solution("X"):
            return -1
    return 0
