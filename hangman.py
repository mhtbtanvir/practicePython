import random
words = ["python", "hangman", "challenge", "programming", "developer"]
chosen_word = random.choice(words)
guessed_words = []
lives = 0
display = ["_" for i in chosen_word]

hangman_stages = ['''
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

while "_" in display and lives <= 6:
    print(f"You have 6 lives.\nlives lost:{lives}\n {hangman_stages[lives]}")
    print(f"word is :{"".join(display)}")
    print(f"guessed words are:{"".join(guessed_words)}")
    guess = input(f"guess a word :").lower()
    guessed_words += guess
    print(f"guessed words are:{"".join(guessed_words)}")

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = letter
                print("good guess")
    else:
        lives += 1
        print("bad guess")
print("the word is:", chosen_word)
if lives == 6:
    print("you lose")
else:
    print("you win")
print("over")
