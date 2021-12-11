def check_board(board, marked):
    for b in range(len(board)):
        for i in range(len(board[b])):
            if board[b][i] in marked:
                board[b][i] = "X"
    for row in board:
        if all(i == "X" for i in row):
            return True, board
    for r in range(len(board)):
        if all(board[i][r] == "X" for i in range(len(board[r]))):
            return True, board
    return False, []

def main():
    file = open("input.txt").read().split("\n\n")
    order = list(map(int, file.pop(0).split(",")))
    boards = []
    for board in file:
        b = []
        for x in board.split("\n"):
            if x != "":
                r = []
                for i in x.split(" "):
                    if i != "":
                        r.append(int(i))
                b.append(r)
        boards.append(b)
    marked = []
    bingo = False
    remaining_sum = 0
    for n in order:
        marked.append(n)
        for board in range(len(boards)):
            isBingo, board = check_board(boards[board], marked)
            if isBingo:
                for i in board:
                    for j in i:
                        if j != "X":
                            remaining_sum += j
                bingo = True
                break
        if bingo:
            break
    print(f"Part1: {remaining_sum * marked[-1]}")
    winning_order = {}
    winning_board = []
    last_won = None
    marked = []
    for n in order:
        bingo = False
        marked.append(n)
        for b in range(len(boards)):
            isBingo, board = check_board(boards[b], marked)
            if isBingo:
                if b not in winning_order.keys():
                    last_won = b
                    winning_order[b] = board
                    winning_board = board
            if len(winning_order.keys()) == len(boards):
                print(winning_board)
                print(boards[last_won])
                bingo = True
                break
        if bingo:
            break
    remaining_sum = 0
    for i in winning_board:
        for j in i:
            if j != "X":
                remaining_sum += j
    print(remaining_sum)
    print(f"Part2: {remaining_sum * marked[-1]}")

if __name__ == "__main__":
    main()