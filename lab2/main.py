from finiteAutomata import *





def show_menu():
    print("1. Show the set of states")
    print("2. Show the alphabet")
    print("3. Show the transition function")
    print("4. Show the initial state")
    print("5. Show the set of final states")
    print("6. Check if is DFA")
    print("7. Check sequence")
    print("8. Exit")

if __name__ == '__main__':
    fa = FiniteAutomata("fa.in")
    option = 0
    while True:
        show_menu()
        option = int(input("Please choose one option "))
        if option == 1:
            print(fa.getStates())
        elif option == 2:
            print(fa.getAlphabet())
        elif option == 3:
            print(fa.getTransitions())
        elif option == 4:
            print(fa.getInitalState())
        elif option == 5:
            print(fa.getFinalStates())
        elif option == 6:
            print(fa.is_DFA())
        elif option == 7:
            sequence = input()
            print(fa.is_sequence_accepted(sequence))
        else:
            break