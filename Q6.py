Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class card(object):
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

        
>>> def getmeaning(self):
        return self.meaning

>>> def __str__(self):
        return self.word + ' : ' + self.getmeaning()

>>> def flashcard(flash, words, meanings):
    flash.append(card(words, meanings))
    return flash

>>> lists = []
>>> y = input("Want to add a flashcard? ")
Want to add a flashcard? Y
>>> while y == 'y' or y == 'Y':
    word = input("Word you want to add to your Flashcards: ")
    meaning = input("Meaning of the word in flashcard: ")
    lists = flashcard(lists, word, meaning)
    y = input("for adding another flashcard, press Y/y :")

Word you want to add to your Flashcards: Game
Meaning of the word in flashcard: Activity
for adding another flashcard, press Y/y :y
Word you want to add to your Flashcards: Batball
Meaning of the word in flashcard: Type of game
for adding another flashcard, press Y/y :n
>>> for el in lists:
    print(el)

    
<__main__.card object at 0x000002169A6DE5C8>
<__main__.card object at 0x000002169A6DEC08>
>>> 