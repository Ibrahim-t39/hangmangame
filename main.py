# Step 1: Import the hangman logo and stages from external files
from hangman_art import logo, stages
print(logo)

# Import the list of words to be used in the game
from hangman_words import word_list

# Step 2: Generate a random word from the word_list
import random
chosen_word = random.choice(word_list)

# Print the chosen word (commented out for actual gameplay)
#print(f'The word was {chosen_word}')

# Step 3: Initialize the display with underscores representing each letter of the word
display = []
for letter in chosen_word:
    display.append("_")

# Print the initial display
print(display)

# Additional display list to keep track of guessed letters
display2 = []

# Set the initial variables for the game
word_choice = len(chosen_word)
n = 6  # Number of lives
end_of_game = False

# Step 4: Main game loop
while not end_of_game:
    # Step 5: Get user input for a letter guess
    guess = input('Guess a letter? ').lower()
    
    # Check if the input is not empty
    if guess != '':
        # Check if only one letter is entered
        if len(guess) == 1:
            # Check if the letter has not been guessed before
            if guess not in display2:
                # Iterate through the chosen word to check for matches
                for position in range(word_choice):
                    letter = chosen_word[position]
                    if guess == letter:
                        display[position] = letter
                        print(display)
                        # Check if all letters have been guessed
                        if '_' not in display:
                            end_of_game = True

                # Check if the guessed letter is not in the word
                if guess not in chosen_word:
                    n -= 1
                    if n == 0:
                        print('You guessed ' + guess + ' which is the wrong answer.')
                        print(f'The word was {chosen_word}. You lose. :(')
                        print(stages[n])
                        end_of_game = True
                    else:
                        print('You guessed ' + guess + ' which is the wrong answer. You lose a life. You have ' + str(n) + ' live(s) left.')
                        print(stages[n])

                # Add the guessed letter to the list of guessed letters
                display2.append(guess)
            else:
                print(f'You have already guessed {guess}, choose a different letter.')
        else:
            print('You can only put one value at a time, re-enter your guess.')
    else:
        print('You cannot leave it blank, re-enter your guess.')

# Step 6: Check if the player won or lost the game
if '_' not in display:
    print('You win! :)')