def validate_input(n):
    try:
        n = int(n)
        if n < 1:
            return False, "Please enter a positive number!"
        elif n > 15:
            return False, "Board size too large! Try N ≤ 15 for reasonable computation time."
        elif n == 2 or n == 3:
            return True, f"Note: {n}-Queens has no solutions, but checking anyway..."
        else:
            return True, f"Solving {n}-Queens problem..."
    except ValueError:
        return False, "Please enter a valid number!"

def get_board_size():
    while True:
        try:
            print("\n" + "=" * 40)
            n = input("Enter board size N (1-15, or 0 to exit): ").strip()
            
            if n == '0':
                return 0
            
            is_valid, message = validate_input(n)
            print(message)
            
            if is_valid:
                return int(n)
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            return 0

def show_summary(solutions, n):
    print(f"\nSUMMARY FOR {n}-QUEENS:")
    print(f"Total solutions found: {len(solutions)}")
    
    if solutions:
        print("First queen positions in each solution:")
        for i, solution in enumerate(solutions[:5], 1):
            for col in range(len(solution)):
                if solution[col][0] == 'Q':
                    print(f"Solution {i}: Queen at row {col + 1}")
                    break
