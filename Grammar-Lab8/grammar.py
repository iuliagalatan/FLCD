import re


class Grammar:
    def __init__(self, filename):
        self.__filename = filename
        self.__nonterminals = []
        self.__startingSymbol = None
        self.__alphabet = []
        self.__productions = {}
        self.readFromFile()

    def readFromFile(self):
        file = open(self.__filename, 'r')
        line = file.readline().strip()

        # read the nonterminals
        delimiters = "->", "{", "}"
        regexPattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(regexPattern, line)

        nonterminals = tokens[2].split(",")

        for nont in nonterminals:
            self.__nonterminals.append(nont)

        #read the alphabet
        line = file.readline().strip()
        delimiters = "->", "{", "}"
        regexPattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(regexPattern, line)
        alphabet = tokens[2].split(",")

        for alpha in alphabet:
            self.__alphabet.append(alpha)

        # read the starting symbol
        line = file.readline().strip()
        token = line.split("=")
        self.__startingSymbol = token[1]

        line = file.readline().strip()
        # read the productions
        for line in file:
            line = line.strip()
            delimiters = "->"
            regexPattern = '|'.join(map(re.escape, delimiters))
            tokens = re.split(regexPattern, line)
            if tokens[2] == '':
                tokens[2] = '-'

            if tokens[0] not in self.__productions.keys():
                self.__productions[tokens[0]] = [tokens[2]]
            else:
                self.__productions[tokens[0]].append(tokens[2])





    def getNonTerms(self):
        return self.__nonterminals

    def getStartingSymb(self):
        return self.__startingSymbol

    def getAlphabet(self):
        return self.__alphabet

    def getProductions(self):
        return self.__productions

    def getProdForNonTerm(self, nonTerminal):
        if nonTerminal not in self.__productions.keys():
            return []
        return self.__productions[nonTerminal]


    def checkCFG(self):
        for key in self.__productions.keys():
            if key not in self.__nonterminals:
                return False
            left = self.__productions[key]
            for t in left:
                t = t.split(" ")
                for symbol in t:
                    if symbol != "":
                        if symbol not in self.__nonterminals and symbol not in self.__alphabet and symbol != "epsilon":
                            return False
        return True

