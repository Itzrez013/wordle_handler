import os

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

    inp = input("\nti (there is) , tin (there is not) , tie (there is exact) , w (words) , clear , -h , exit , restart  : ")
    w = True


    if inp == "ti":

        char = input("there is a what? ( 0 for cancel ) : ")
        if char not in there_is and char!="0" :
            there_is.append(char)




    elif inp == "tin":

        char = input("there is what not? ( 0 for cancel ) : ")

        if char!="0":
            position = input("where? ( just enter for all indexes. ) ( 0 for cancel ) : ")
            if position!='0':
                if position=="":

                    for i in range(1,6):
                        there_is_not[i]+=char

                else:
                    position=int(position)

                if char and position in there_is_not:
                    there_is_not[position] += char



    elif inp == "tie":

        char = input("oh yeah? what is there? ( 0 for cancel ) : ")

        if char!='0':
            position = int(input("really? where? ( 0 for cancel ) : "))
            if position in there_is_exact and position!='0':
                there_is_exact[position] = char



    elif inp=="clear":
        os.system('cls' if os.name == 'nt' else 'clear')


    elif inp=="restart":
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



    elif inp == "exit":
        break


    elif inp=="-h":
        print("""You can use 'ti' when you know a letter is in the word but don't know its exact position.
You can use 'tin' when you're sure that a letter is not in a specific position.
You can leave the index empty after using 'tin' to apply the rule to all positions.
You can use 'tie' when you're sure about a letter at a specific position.
You can use 'w' to see which words remain. """)


    elif inp == 'w':
        print("\nPossible words:")
        print(w2)
        w=False

    else:
        print("Unknown command")
        continue


    w2 = filter_words(words)



    if w:
        print("\nThere is:")
        print(there_is)

        print("\nThere is NOT:")
        print(there_is_not)

        print("\nThere is EXACT:")
        print(there_is_exact)

        print("\nNumber of possible words:")
    print(len(w2))
