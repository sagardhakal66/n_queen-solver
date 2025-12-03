def display_solution(solution, solution_number=1):
    n = len(solution)
    
    print(f"\nSOLUTION {solution_number}:")
    print("+" + "---+" * n)
    
    for row in solution:
        print("|", end="")
        for cell in row:
            if cell == 'Q':
                print(" Q |", end="")
            else:
                print("   |", end="")
        print()
        print("+" + "---+" * n)

def display_all_solutions(solutions):
    print(f"\nDISPLAYING ALL {len(solutions)} SOLUTIONS:")
    print("=" * 50)
    
    for i, solution in enumerate(solutions, 1):
        display_solution(solution, i)
        if i < len(solutions):
            print("\n" + "-" * 30)

def show_solution_choice(solutions):
    if not solutions:
        print("No solutions to display!")
        return
    
    print(f"\nFound {len(solutions)} solutions!")
    
    if len(solutions) == 1:
        display_solution(solutions[0])
        return
    
    while True:
        try:
            print("\nChoose display option:")
            print("1 - Show first solution only")
            print("2 - Show all solutions")
            print("3 - Show specific number of solutions")
            
            choice = input("Enter your choice (1/2/3): ").strip()
            
            if choice == '1':
                display_solution(solutions[0])
                break
            elif choice == '2':
                display_all_solutions(solutions)
                break
            elif choice == '3':
                num = int(input(f"How many solutions to show? (1-{len(solutions)}): "))
                if 1 <= num <= len(solutions):
                    for i in range(num):
                        display_solution(solutions[i], i+1)
                    break
                else:
                    print("Invalid number!")
            else:
                print("Please enter 1, 2, or 3!")
                
        except ValueError:
            print("Please enter a valid number!")
