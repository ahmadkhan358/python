class BollywoodGame():

    def __init__(self, word):
        self.bollywood = 'BollywoodGame'
        self.word = word

    def __str__(self):
        return self.word
    
    def find_occurences(self, letter):
        indexes = []
        for i in range(len(self.word[1:])):
            if self.word[i+1] == letter:
                indexes.append(i)

        return indexes


    def play(self):
        print_word = [' '] * len(self.word)
        print_word[0] = self.word[0]
        word_to_guess = self.word[1:]
        length_of_word = len(word_to_guess)
        bolly = len(self.bollywood)
        print(print_word)
        print(self.bollywood)
        print('\n')
        while True:
            
            letter = input("Input letter ? ")[0]
            if letter in word_to_guess:
                letter_count = word_to_guess.count(letter)
                word_to_guess= word_to_guess.replace(letter, '')
                length_of_word -= letter_count
                indexes = self.find_occurences(letter)
                for i in indexes:
                    print_word[i+1] = letter
            else:
                self.bollywood = self.bollywood[1:]
                bolly -= 1

            print(print_word)
            print(self.bollywood)
            print('\n')
            if bolly == 0:
                print("Loser")
                print(f"The word was {self.word}")
                break
        
            if length_of_word == 0:
                print("You guessed it correctly")
                break


if __name__ == "__main__":
    game_init = BollywoodGame('black')
    game_init.play()
    