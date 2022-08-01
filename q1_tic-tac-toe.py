# import numpy as np

HORIZONTAL_WALL = "-"
VERTICAL_WALL = "|"
CORNER = "+"
EMPTY = " "
CELL_SIZE = 3
PIECE = ("O", "X")


def print_grid(puzzle: list):
    board_repr = ""
    horizontal_border = (CORNER + HORIZONTAL_WALL * CELL_SIZE) * 3 + \
                        CORNER + "\n"
    board_repr += horizontal_border
    for row in range(3):
        board_repr += VERTICAL_WALL
        for col in range(3):
            cell_index = col + row * 3
            cell_content = puzzle[cell_index]
            board_repr += f" {cell_content} {VERTICAL_WALL}"
        board_repr += "\n" + horizontal_border
    print(board_repr, end="")

def place_piece(puzzle: list, turn: bool, index: int) -> bool:
    if puzzle[index] == ' ':
        puzzle[index] = PIECE[turn]
        return not turn
    return turn
        
def check_over(puzzle: list) -> bool:
    # return np.logical_or(
    #     puzzle[0] == puzzle[1] == puzzle[2] != ' ', 
    #     puzzle[3] == puzzle[4] == puzzle[5] != ' ',
    #     puzzle[6] == puzzle[7] == puzzle[8] != ' ',
    #     puzzle[0] == puzzle[3] == puzzle[6] != ' ',
    #     puzzle[1] == puzzle[4] == puzzle[7] != ' ',
    #     puzzle[2] == puzzle[5] == puzzle[8] != ' ',
    #     puzzle[0] == puzzle[4] == puzzle[8] != ' ',
    #     puzzle[2] == puzzle[4] == puzzle[6] != ' ')
    return puzzle[0] == puzzle[1] == puzzle[2] != ' ' \
        or puzzle[3] == puzzle[4] == puzzle[5] != ' ' \
        or puzzle[6] == puzzle[7] == puzzle[8] != ' ' \
        or puzzle[0] == puzzle[3] == puzzle[6] != ' ' \
        or puzzle[1] == puzzle[4] == puzzle[7] != ' ' \
        or puzzle[2] == puzzle[5] == puzzle[8] != ' ' \
        or puzzle[0] == puzzle[4] == puzzle[8] != ' ' \
        or puzzle[2] == puzzle[4] == puzzle[6] != ' '

def game_over(puzzle: list):
    print_grid(puzzle)
    print("game over!")
    main()

def optimaliser(puzzle, turn) -> int:
    for i in range(len(puzzle)):
        # turn can win next move, place there
        local_puzzle = puzzle.copy()
        place_piece(local_puzzle, turn, i)
        if check_over(local_puzzle):
            return i
        # (not turn) can win next move, place there
        local_puzzle = puzzle.copy()
        place_piece(local_puzzle, not turn, i)
        if check_over(local_puzzle):
            return i
    # middle empty, place there
    if puzzle[4] == ' ':
        return 4 
    # random empty place
    for i in range(len(puzzle)):
        if puzzle[i] == ' ':
            return i

def main():
    num_player = int(input("number of players: "))
    puzzle = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    turn = False
    if num_player == 0:
        while not check_over(puzzle):
            print_grid(puzzle)
            index = int(input("index (0~8): "))
            turn = place_piece(puzzle, turn, index)
        game_over(puzzle)

    if num_player == 1:
        player_turn = int(input("player turn (0/1): "))
        while not check_over(puzzle):
            print_grid(puzzle)
            if turn == player_turn:
                index = int(input("index (0~8): "))
            else:
                index = optimaliser(puzzle, turn)
            turn = place_piece(puzzle, turn, index)
        game_over(puzzle)


if __name__ == '__main__':
    main()


