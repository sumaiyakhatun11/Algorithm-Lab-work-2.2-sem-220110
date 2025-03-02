def print_solution1(board,n1):
    for i in range(n1):
        for j in range(n1):
            if board[i][j]==1:
                print('Q',end=' ')
            else:
                print('.',end=' ')
        print()

    print()


def is_safe1(board,n,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False

    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False

    for i,j in zip(range(row,n,1),range(col,-1,-1)):
        if board[i][j]==1:
            return False

    return True




def solve_n_q_util1(board,n,col):
    if col>=n:
        return True
    for i in range(n):
        if is_safe1(board,n,i,col):
            board[i][col]=1
            if solve_n_q_util1(board,n,col+1):
                return True
            board[i][col]=0

    return False




def solve_n_q():
    n1=int(input('Enter Board Size: '))
    board=[[0 for _ in range(n1)] for _ in range(n1)]

    if solve_n_q_util1(board,n1,0)==False:
        print('solution does not exist')

    else:
        print_solution1(board,n1)

if __name__ == '__main__':
    solve_n_q()