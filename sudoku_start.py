import numpy as np

def print_sudoku(sudoku):
    for row in sudoku:
        print(" ".join(map(str, row)))

def is_valid_move(sudoku, row, col, num):
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(sudoku, row, col, num):
                        sudoku[row][col] = num
                        if solve_sudoku(sudoku):
                            return True
                        sudoku[row][col] = 0
                return False
    return True

if __name__ == "__main__":
    sudoku = np.zeros((9, 9), dtype=int)
    
    print("Введите судоку (9x9), используя 0 для пустых клеток:")
    input_string = ""
    for i in range(9):
        input_string += input() + "\n"

    input_lines = input_string.strip().split("\n")
    for i in range(9):
        row = input_lines[i].split()
        for j in range(9):
            sudoku[i][j] = int(row[j])

    print("\nИсходное судоку:")
    print_sudoku(sudoku)

    if solve_sudoku(sudoku):
        print("\nРешение судоку:")
        print_sudoku(sudoku)
    else:
        print("\nСудоку не имеет решения.")
