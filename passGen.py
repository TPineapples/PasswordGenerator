import random

def outPass(words):
    for i in range(len(words)):
        print(str(i)+"\t"+words[i])

def genNextChar(type):
    numList = list(range(0, 10))
    charList = list("abcdefghijklmnopqrstuvwxyz")
    symbolList = list("!@#$%^&*()-_=+,.<>/;:'\"[]{}|`~")

    if type == "char":
        return random.choice(charList)
    if type == "num":
        return random.choice(numList)
    if type == "case":
        return random.choice(charList).upper()
    if type == "sym":
        return random.choice(symbolList)


def genPass(count, min, max, numbers, casing, symbols):
    types = ["char"]
    words = []
    score = 0

    if numbers:
        score += 1
        types.append("num")
    if casing:
        score += 1
        types.append("case")
    if symbols:
        score += 1
        types.append("sym")

    while len(words) != count:
        newPass = ""
        size = random.randint(min, max)
        while len(newPass) != size:
            nextCharType = types[random.randint(0,score)]
            newPass += str(genNextChar(nextCharType))
        words.append(newPass)
        print("Generated " + str(len(words)) + " passwords out of " + str(count))

    print("Completed Password Generation")
    outPass(words)






def wizMod(min,max):
    print("The following 3 questions require yes and no answers\n"
          "For yes please type 'y'\n"
          "For no please type 'n'")
    numbers = input("Should the password contain numbers?\n"
                    "> ")
    if numbers == 'y':
        numbers = True
    else:
        numbers = False

    casing = input("Should the password contain capital letters?\n"
                   "> ")
    if casing == 'y':
        casing = True
    else:
        casing = False

    symbols = input("Should the password contain symbols?\n"
                    "> ")
    if symbols == 'y':
        symbols = True
    else:
        symbols = False

    count = abs(int(input("Finally, how many passwords should we generate? (Please enter a number between 1 and 999\n"
                  "> ")))
    if count < 1:
        count = 1
    if count > 999:
        count = 999

    genPass(count,min,max,numbers,casing,symbols)



def wiz():
    print("Lets begin!\n"
          "Do you want the password to have a specific size (a) or do you want a random size within a range (b)?\n"
          "If specific type 'a'\n"
          "If a range type 'b'\n")
    flag = True
    while flag:
        opt = input("> ")
        if opt == 'a':
            flag = False
            size = abs(int(input("Please enter the size of the desired password\n"
                         "> ")))
            if size < 3:
                size = 3

            wizMod(size,size)

        elif opt == 'b':
            flag = False
            min = abs(int(input("Please enter the minimum size of the desired password\n"
                            "> ")))
            max = abs(int(input("Please enter the maximum size of the desired password\n"
                            "> ")))
            if min > max:
                min,max = max,min

            wizMod(min,max)

        else:
            flag = True
            print("Please enter an appropriate option\n"
                  "For specific size type 'a'\n"
                  "For specific range type 'b'\n")


#main
print("Welcome to passGen\n"
      "If you are aware of the parameters please enter the correct inputs\n"
      "Alternatively please type -wiz to go through the wizard")
args = input("> ")
if args == "-wiz":
    wiz()
else:
    print("Not yet implemented")