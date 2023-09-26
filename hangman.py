#Step 1

from hangman_art import logo, stages
print(logo)

from hangman_words import word_list

#Generate a random word from word_list.
import random
chosen_word = random.choice(word_list)
#print(f'The word was {chosen_word}')

#Print out 'chosen_word' number of dashes.
display = []
for letter in chosen_word:
    display.append("_")

print(display)

display2 = []

#Check if user's guess is in word.
word_choice = len(chosen_word)
n = 6
#blanks = '_' in display
end_of_game = False
while not end_of_game:
    guess = input('Guess a letter? ').lower()
    if guess != '':
        if len(guess) == 1:
                if guess not in display2:
                    for position in range(word_choice):
                        letter = chosen_word[position]
                        if guess == letter:
                            display[position] = letter
                            print(display)
                            if '_' not in display:
                                end_of_game = True

                    if guess not in chosen_word:
                        n -= 1
                        if n == 0:
                            print('You guessed '+ guess +' which is the wrong answer.')
                            print(f'The word was {chosen_word}. You lose. :(')
                            print(stages[n]) 
                            end_of_game = True
                        else:  
                            print('You guessed ' + guess + ' which is the wrong answer. You lose a life. You have ' + str(n) +' live(s) left.')
                            print(stages[n])
                    display2.append(guess)
                else:
                    print(f'You have already guessed {guess}, choose a different letter.')
        else:
            print('You can only put one value at a time, re enter your guess.')
    else:        
        print('You cannot leave it blank, re enter your guess.')
    
            
if '_' not in display:         
    print('You win! :)')