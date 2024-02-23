looper = True
while looper:
    word = input()
    if word == "quit!":
        break
    elif len(word) > 3:
        if word[-3] not in "aeiouy" and word[-2:] == "or":
            print(word.replace("or", "our"))
        else:
            print(word)
    else:
        print(word)
