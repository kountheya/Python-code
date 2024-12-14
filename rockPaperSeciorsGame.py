import tkinter as tk
import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to update the score
def update_scores(result, scores):
    if result == "You win!":
        scores['user'] += 1
    elif result == "You lose!":
        scores['computer'] += 1

# Function to display the score and result
def display_results(result, user_choice, computer_choice):
    result_label.config(text=f"Result: {result}")
    user_choice_label.config(text=f"You chose: {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice.capitalize()}")
    score_label.config(text=f"Score - You: {scores['user']} | Computer: {scores['computer']}")

# Function to play the game when a button is clicked
def play(choice):
    user_choice = choice
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    update_scores(result, scores)
    display_results(result, user_choice, computer_choice)

# Function to reset the game
def reset_game():
    scores['user'] = 0
    scores['computer'] = 0
    result_label.config(text="Result: ")
    user_choice_label.config(text="You chose: ")
    computer_choice_label.config(text="Computer chose: ")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Setting up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Game score
scores = {'user': 0, 'computer': 0}

# Score label
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 16))
score_label.pack(pady=20)

# Result labels
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=5)

user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 14))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 14))
computer_choice_label.pack(pady=5)

# Buttons for the choices
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", width=10, height=2, font=("Arial", 12), bg="lightblue", command=lambda: play('rock'))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", width=10, height=2, font=("Arial", 12), bg="lightgreen", command=lambda: play('paper'))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, height=2, font=("Arial", 12), bg="lightcoral", command=lambda: play('scissors'))
scissors_button.grid(row=0, column=2, padx=10)

# Reset button
reset_button = tk.Button(root, text="Reset Game", width=20, height=2, font=("Arial", 12), bg="lightgray", command=reset_game)
reset_button.pack(pady=20)

# Run the application
root.mainloop()
