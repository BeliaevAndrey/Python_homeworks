def display(board: list[str]) -> None:
    print('\n---+---+---\n'.join(
        [' ' + ' | '.join(board[i: i+3]) for i in range(0, len(board), 3)])
    )


def print_crd():
    display([f'{x}' for x in range(1, 10)])


def player_turn(board: list[str]):
    while True:
        pos = input("Input cell number: ")
        if pos.isdigit() and 0 < int(pos) < len(board) + 1:
            return int(pos)