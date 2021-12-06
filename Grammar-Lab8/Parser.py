class Parser:
    def __init__(self, grammar):
        self.__grammar = grammar

    def closure(self, productions):

        if productions == []:
            return None
        C = productions
        going = True

        while going:
            going = False
            for prod in C:
                elem = prod[1][0]
                dotInd = elem.find('.')
                alpha = elem[:dotInd]
                bBeta = elem[dotInd + 1:].strip()

                
                if len(bBeta) != 0:
                    B = bBeta[0]
                    if self.__grammar.isTerminal(B):
                        continue
    
                    prodsforB = self.__grammar.getProdForNonTerm(B)
    
                    for p in prodsforB:
                        for t in p:
                            production = (B, ['.' + t])
                            if production not in C:
                                C += [production]
                                going = True
        return C

    def getCannonicalCollection(self):
        C = [self.closure([('S1', ['.'+ self.__grammar.getStartingSymb()])])]

        done = False

        while not done:
            done = True

            for state in C:
                for x in self.__grammar.getNonTerms() + self.__grammar.getAlphabet():
                    nextState = self.goTo(state, x)
                    if nextState is not None and nextState not in C:
                        C = C + [nextState]
                        done = False
        return C


    def goTo(self, state, symbol):
        #mutam punctul daca symbol == primul symbol de dupa punct
        C = []
        for production in state:
            index = production[1][0].find('.')
            alpha = production[1][0][:index]
            Xbeta = production[1][0][index + 1:].strip()

            if len(Xbeta)!= 0:
                X, beta = Xbeta[0], Xbeta[1:]
                if X == symbol:
                    if alpha != "":
                        resultProd = (production[0], [alpha +' ' +X + '.' + beta])
                    else:
                        resultProd = (production[0], [alpha +X + '.' + beta])
                    C = C + [resultProd]

        return self.closure(C)

    def Table(self):
        states = self.getCannonicalCollection()
        table = [{} for ind in range(len(states))]

        for state in states:
            print(state)
        index  = 0

        for state in states:
            FirstRule = 0
            SecondRule = 0
            ThirdRule = 0

            for prod in state:
                if prod[0] == 'S1':
                    ok= True
                index = prod[1][0].find('.')
                alpha = prod[1][0][:index]
                beta = prod[1][0][index + 1:]
                if len(beta) != 0:
                    FirstRule += 1
                else:
                    if prod[0] != 'S1':
                        SecondRule += 1
                        productionIndex = self.__grammar.p.index([prod[0], alpha])

                    elif alpha == self.__grammar.getStartingSymb():
                        ThirdRule += 1

            if FirstRule == len(state):
                table[index]['action'] = 'shift'

            elif SecondRule == len(state):
                table[index]['action'] = 'r' + str(productionIndex)

            elif ThirdRule == len(state):
                table[index]['action'] = 'acc'

            else:
                raise (Exception('No action for state ' + str(index) + ' ' + str(state)))

            for symbol in self.__grammar.getNonTerms() + self.__grammar.getAlphabet():
                nextState = self.goTo(state, symbol)
                if nextState in states:
                    table[index][symbol] = states.index(nextState)

            index = index + 1
        return table


    def parse(self, inputSequence):
        table = self.Table()

        self.parsingStack = ['0']
        self.inputStack = [symbol for symbol in inputSequence]
        self.output = []


        print(table)

        while len(self.parsingStack) != 0:
            state = int(self.parsingStack[-1])

            if len(self.inputStack) > 0:
                symbol = self.inputStack.pop(0)
            else:
                symbol = None
            if  symbol != None and table[state][symbol] and table[state]["action"] == "shift":
                self.parsingStack.append(symbol)
                self.parsingStack.append( str(table[state][symbol]))

            elif table[state]["action"] == "acc":
                if (len(self.inputStack)) != 0:
                    raise Exception("somethink went wrong")
                self.parsingStack = []
            else:
                try:
                    reduceIndex = int(table[state]["action"][1:])
                except:
                    print("Exception!!!")
                production = self.__grammar.p[reduceIndex]
                self.parsingStack.pop()
                toRemoveFromWorkingStack = [symbol for symbol in production[1]]
                toRemoveFromWorkingStack = ' '.join(toRemoveFromWorkingStack).split()

                while len(toRemoveFromWorkingStack) > 0 and len(self.parsingStack) > 0:
                    if(self.parsingStack[-1].isnumeric()):
                        self.parsingStack.pop()
                    if self.parsingStack[-1] == toRemoveFromWorkingStack[-1]:
                        toRemoveFromWorkingStack.pop()
                    self.parsingStack.pop()

                if len(toRemoveFromWorkingStack) != 0:
                    raise (Exception('Cannot Parse reduce'))

                idx = self.parsingStack[-1]
                self.inputStack.insert(0, production[0])
                self.output.insert(0, str(reduceIndex))

        return self.output




