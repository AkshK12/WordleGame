import random


#select a random word from 5words_alpha.txt
with open("./5words_alpha.txt") as f:
    words=set(map(
        lambda x: x.strip(),
        f.readlines()
    ))


chosen_word=random.choice(list(words))

#Trial Method
trial_index=0
MAX_TRIALS=5
while trial_index<MAX_TRIALS:

    trial_word=input(f"ENTER {trial_index+1}: ")
    if len(trial_word) != 5:
        print("INVALID WORD LENGTH")
        continue
    if trial_word not in words:
        print("INVALID WORD ENTER AGAIN")
        continue
    trial_index += 1
    if trial_word == chosen_word:
        print(f"CORRECT WORD GUESSED IN {trial_index}!!")
        break

    matches = {}
    for i in range(5):
        if trial_word[i] == chosen_word[i]:
            matches.update({i: 2})
        elif trial_word[i] in chosen_word:
            matches.update({i: 1})
        else:
            matches.update({i: 0})
    
    for i,c in enumerate(trial_word):
        if matches[i] == 2:
            print(f"\033[32m{c}\033[0m",end="")
        elif matches[i] == 1:
            print(f"\033[33m{c}\033[0m",end="")
        else:
            print(f"\033[31m{c}\033[0m",end="")
    print()
print(chosen_word)



            



