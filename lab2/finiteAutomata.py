import re


class FiniteAutomata:
    def __init__(self, file):
        self.__Q = []  #states
        self.__S = {}  #transitions
        self.__E = []   #alphabet
        self.__F = []  #final states
        self._q0 = "" #initial state
        self.__file = file
        self.wrong = False

        if self.readFile() == False:
            self.wrong = True

    def getLine(self, line):
        line = line.split('=')
        substring = line[1]
        substring = substring.split()
        return substring


    def readFile(self):
        with open(self.__file) as file:
            self.__Q = self.getLine(file.readline())
            self.__E = self.getLine(file.readline())
            self.__q0 = file.readline().split('=')[1].strip()

            if self.__q0 not in self.__Q:
                return False

            substring = self.getLine(file.readline())
            for state in substring:
                if state not in self.__Q:
                    return False

            self.__F = substring

            file.readline()

            self.__S = {}

            for line in file:
                line = line.strip()
                delimiters = "(", "=", ")",
                regexPattern = '|'.join(map(re.escape, delimiters))
                tokens = re.split(regexPattern, line)
                tokens = list(filter(None, tokens))
                key = tokens[1].split(",")
                state1 = key[0]
                symbol = key[1]
                state2 = tokens[2]
                if state1 not in self.__Q:
                    return False
                if state2 not in self.__Q:
                    return False

                if (state1, symbol) in self.__S.keys():
                    state2check = self.__S.get((state1, symbol))
                    if state in state2check:
                        self.__S[(state1, symbol)].append(state2)
                else:
                    self.__S[(state1, symbol)] = [state2]


    def getStates(self):
        return self.__Q

    def getAlphabet(self):
        return self.__E

    def getTransitions(self):
        return self.__S

    def getInitalState(self):
        return self.__q0

    def getFinalStates(self):
        return self.__F

    def is_DFA(self):
        for elem in self.__S.keys():
            if len(self.__S[elem]) > 1:
                return False
        return True

    def is_seq_accepted(self, sequence):
        state = self.__q0
        for symbol in sequence:
            if (state, symbol) in self.__S.keys():
                state = self.__S[(state, symbol)][0]
            else:
                return False
        if state in self.__F:
            return True
        return False


    def is_sequence_accepted(self, sequence):
        if self.is_DFA():
            return self.is_seq_accepted(sequence)
        return False

