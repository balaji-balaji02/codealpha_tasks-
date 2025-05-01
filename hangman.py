import random

word_list = ["python", "hangman", "college", "project", "gamer"]
chosen_word = random.choice(word_list)
guessed_letters = []
tries = 6

def display_word():
    return " ".join([letter if letter in guessed_letters else "_" for letter in chosen_word])

print("🎉 Welcome to Hangman!")
print("You have", tries, "tries to guess the word.")
print(display_word())

while tries > 0:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a **single alphabet letter**.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print("❌ Wrong guess. Tries left:", tries)

    print(display_word())

    if all(letter in guessed_letters for letter in chosen_word):
        print("🎊 Congratulations! You guessed the word:", chosen_word)
        break
else:
    print("💀 Game over! The word was:", chosen_word)
