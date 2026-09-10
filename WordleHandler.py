with open("wordle.txt") as f:
    words = [
        line.strip()
        for line in f
        if len(line.strip().lower()) == 5
    ]


there_is = []

there_is_not = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: ""
}

there_is_exact = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: ""
}


def filter_words(words):


    for char in there_is:
        words = [
            word
            for word in words
            if char in word
        ]



    for position, chars in there_is_not.items():

        if chars:
            words = [
                word
                for word in words
                if word[position - 1] not in chars
            ]



    for position, char in there_is_exact.items():

        if char:
            words = [
                word
                for word in words
                if word[position - 1] == char
            ]


    return words


while True:

    inp = input("\nti , tin , tie , w , exit : ")



    if inp == "ti":

        char = input("there is a what? : ")

        if char not in there_is:
            there_is.append(char)




    elif inp == "tin":

        char = input("there is what not? : ")

        position = input("where? ( just enter for all indexes. ) : ")


        if position=="":
            for i in range(1,6):
                there_is_not[i]+=char

        else:
            position=int(position)

        if position in there_is_not:
            there_is_not[position] += char



    elif inp == "tie":

        char = input("oh yeah? what is there? : ")

        position = int(input("really? where? : "))

        if position in there_is_exact:
            there_is_exact[position] = char



    elif inp == "exit":
        break


    elif inp == 'w':
        print("\nPossible words:")
        print(w2)


    else:
        print("Unknown command")
        continue


    w2 = filter_words(words)




    print("\nThere is:")
    print(there_is)

    print("\nThere is NOT:")
    print(there_is_not)

    print("\nThere is EXACT:")
    print(there_is_exact)

    print("\nNumber of possible words:")
    print(len(w2))