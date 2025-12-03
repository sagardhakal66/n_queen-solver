from n_queens import solve_n_queens
from visualizer import show_solution_choice
from utils import get_board_size, show_summary

def main():
    print("N-QUEENS PROBLEM SOLVER By Sagar Dhakal")
    print("=" * 50)
    print("Place N queens on N×N chessboard")
    print("so no two queens attack each other!")
    
    while True:
        n = get_board_size()
        
        if n == 0:
            print("Thanks for using N-Queens Solver!")
            break
        
        print(f"\nSolving {n}-Queens problem...")
        solutions = solve_n_queens(n)
        
        show_summary(solutions, n)
        show_solution_choice(solutions)
        
        continue_choice = input("\nSolve another N-Queens? (y/n): ").lower().strip()
        if continue_choice not in ['y', 'yes']:
            print("Byebye!")
            break

if __name__ == "__main__":
    main()
