class Solution(object):    
    def solveNQueens(self, n):
        """
        The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

        Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

        Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
        
        Input: n = 4
        Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
        
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        queens = ['#'] * n
        
        def dfs(index):
            if index == len(queens):
                res.append(queens[:])
                print(queens, "True")
                return
            for i in range(len(queens)):
                queens[index] = i
                if valid(index):
                    dfs(index+1)
                    
        def valid(n):
            for i in range(n):
                if abs(queens[n] - queens[i]) == n-i: # same diagonal
                    print(queens, "False")
                    return False
                if queens[n] == queens[i]: # same column
                    print(queens, "False")
                    return False
            return True
        
        def make_board(queens):
            n = len(queens)
            board = []
            board_temp = [['.'] * n for _ in range(n)]
            for row, col in enumerate(queens):
                board_temp[row][col] = 'Q'
            for row in board_temp:
                board.append("".join(row))
            return board
        
        def make_all_boards(res):
            actual_boards = []
            for queens in res:
                actual_boards.append(make_board(queens))
            return actual_boards
        
        dfs(0)
        return make_all_boards(res)
    
print(Solution().solveNQueens(4))
    