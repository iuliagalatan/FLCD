from grammar import *
from Parser import *
def menu():
    print("0. Exit")
    print("1. Set of NonTerminals")
    print("2. The alphabet")
    print("3. Starting Symbol")
    print("4. Productions")
    print("5. Get productions for a given non-terminal")
    print("6. Parse sequence")


if __name__ == '__main__':
    print("Test Grammar")
    menu()

    option=-1


    grammar = Grammar("g3.in")
    parser = Parser(grammar)
    #parser.getCannonicalCollection()


    print(grammar.checkCFG())
    while(option!=0):
        option=int(input("option:"))
        if option==1:
            print(grammar.getNonTerms())
        elif option==2:
            print(grammar.getAlphabet())
        elif option==3:
            print(grammar.getStartingSymb())
        elif option==4:
            print(grammar.getProductions())
        elif option==5:
            nonterm = input("non-terminal")
            print(grammar.getProdForNonTerm(nonterm))
        elif option ==6:

            sequence = input("sequence for lr(0) parser:")
            try:
                parser.parse(sequence)
            except Exception as e:
                print(e)
