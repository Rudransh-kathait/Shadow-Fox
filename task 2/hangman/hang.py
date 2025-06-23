import random

words =['blue','green','pink','purple','yellow','black','white','violet','grey']
create_word =  random.choice(words)

#print(create_word)
lives= len(create_word)
#print(lives)
letters=set()

while lives:
    display = [ch if ch in letters else "_" for ch in create_word]
    print("Word so far:", " ".join(display))
    if "_" not in display:
        print("You guessed it \n")
        break;
    
    found= input("Guess the letter in the word \n").lower()
    if found in letters:
        print("You already found a letter \n")
    
    letters.add(found)
    if found in create_word:
        continue
    else:
        lives -= 1

    print(f"Lives remaining: {lives}")
