import random

from hangman_words import words

from hangman_art import stages, logo
print(logo)

eog = False

cword = random.choice(words)
wl=len(cword)
lives = 6

print(f"psst, the solution is {cword}")

display =[]
for _ in range(wl):
    display += "_"
while not eog:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You've already guessed {guess}")
    for i in range(wl):
        j = cword[i]
        if j == guess:
            display[i] = j
    if guess not in cword:
      print(f"You guessed {guess}, that's not in the owrd. You lose a life")
      lives -=1
      if lives ==0:
          eog = True
          print("You lose")

        
    print(f"{' '.join(display)}")

    if "_" not in display:
        eog = True
        print("You win.")

    print(stages[lives])