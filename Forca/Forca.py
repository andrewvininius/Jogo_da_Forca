import random

def choose_word():
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def is_word_complete(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

def hangman():
    word = choose_word()
    max_attempts = 6
    guessed_letters = []
    
    print("Bem-vindo ao jogo da forca!")
    
    while max_attempts > 0:
        display = display_word(word, guessed_letters)
        print("\nPalavra: " + display)
        guess = input("Digite uma letra: ").lower()
        
        if guess in guessed_letters:
            print("Você já tentou essa letra. Tente outra.")
        else:
            guessed_letters.append(guess)
            if guess in word:
                print("Letra correta!")
                if is_word_complete(word, guessed_letters):
                    print("\nParabéns! Você adivinhou a palavra correta: " + word)
                    break
            else:
                max_attempts -= 1
                print("Letra incorreta! Você tem mais", max_attempts, "tentativas.")
    
    if max_attempts == 0:
        print("\nVocê perdeu! A palavra correta era:", word)

if __name__ == "__main__":
    hangman()
