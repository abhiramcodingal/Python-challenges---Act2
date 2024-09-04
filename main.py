class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return " " + self.word + " ( " + self.meaning + " )"
    
flash = []
print("Welcome to flashcard application.")
while True:
    word = input("Enter the word you want to add: ")
    meaning = input("Enter the meaning of the above word: ")
    flash.append(flashcard(word,meaning))
    repeat = int(input("If you want to enter again, enter 1 otherwise, enter 0: "))
    if repeat == 0:
        break

print("Your flashcards are:- ")
for i in flash:
    print(">" ,i)

print("Thank you for using flashcard application.")