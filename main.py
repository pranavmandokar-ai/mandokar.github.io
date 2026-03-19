import time
import os

# --- The Questions ---
QUESTIONS = {
    "World": [
        {"q": "Which planet is the Red Planet?", "a": ["Mars", "Venus", "Jupiter", "Saturn"], "correct": 1},
        {"q": "What is the capital of France?", "a": ["Berlin", "Madrid", "Paris", "Rome"], "correct": 3},
        {"q": "Who painted the Mona Lisa?", "a": ["Van Gogh", "Da Vinci", "Picasso", "Monet"], "correct": 2},
    ],
    "Science": [
        {"q": "What is the chemical symbol for Gold?", "a": ["Gd", "Ag", "Au", "Fe"], "correct": 3},
        {"q": "What is the hardest rock?", "a": ["Gold", "Iron", "Diamond", "Coal"], "correct": 3},
    ],
    "Gadgets": [
        {"q": "Who made the first Linux?", "a": ["Steve Jobs", "Linus Torvalds", "Bill Gates", "Elon Musk"], "correct": 2},
        {"q": "What does HTTP stand for?", "a": ["HyperText Transfer Protocol", "High Tech Protocol", "Hyperlink Text", "None"], "correct": 1},
    ]
}

def clear_screen():
    # Clears the terminal screen so it looks clean
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header(lives, score):
    print("=" * 30)
    print(f" LIVES: {'❤️ ' * lives} | SCORE: {score}")
    print("=" * 30)

def run_quiz():
    score = 0
    lives = 3
    
    clear_screen()
    print("Welcome to the Python Quiz Game!")
    print("\nPick a category:")
    
    categories = list(QUESTIONS.keys())
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    
    choice = input("\nEnter number (1-3): ")
    
    # Validate category choice
    if not choice.isdigit() or int(choice) not in range(1, len(categories) + 1):
        print("Invalid choice! Restarting...")
        time.sleep(1)
        return run_quiz()
    
    selected_cat = categories[int(choice) - 1]
    quiz_list = QUESTIONS[selected_cat]

    for item in quiz_list:
        if lives <= 0:
            break
            
        clear_screen()
        show_header(lives, score)
        print(f"Category: {selected_cat}\n")
        print(f"QUESTION: {item['q']}")
        
        # Show multiple choice options
        for i, option in enumerate(item['a'], 1):
            print(f"  {i}) {option}")
        
        start_time = time.time()
        user_ans = input("\nYour answer (1-4): ")
        end_time = time.time()
        
        # Calculate how fast they answered
        time_taken = int(end_time - start_time)
        
        if user_ans.isdigit() and int(user_ans) == item['correct']:
            # Correct! Give bonus for speed
            bonus = max(0, 15 - time_taken) 
            points = 10 + bonus
            score += points
            print(f"\n✅ CORRECT! +{points} points")
        else:
            lives -= 1
            print(f"\n❌ WRONG! The right answer was: {item['a'][item['correct']-1]}")
            print(f"You lost a life!")
            
        time.sleep(2)

    # End of Game
    clear_screen()
    print("=" * 30)
    if lives > 0:
        print("🎉 CONGRATULATIONS! YOU FINISHED!")
    else:
        print("💀 GAME OVER! You ran out of lives.")
        
    print(f"\nFINAL SCORE: {score}")
    print("=" * 30)
    
    retry = input("\nPlay again? (y/n): ")
    if retry.lower() == 'y':
        run_quiz()

if __name__ == "__main__":
    run_quiz()
