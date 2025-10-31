import random
words = ["apple", "train", "pizza", "chair", "phone"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []
print("Welcome to Hangman!")
while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)
    print("Used letters:", used_letters)
    guess = input("Enter a letter: ").lower()
    if guess in used_letters:
        print("You already guessed that letter!")
        continue
    used_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print("Wrong guess!")
if "_" not in guessed:
    print("\nCongratulations, You Win! The word was:", word)
else:
    print("\nSorry, Game Over! The word was:", word)
