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
                bBeta = elem[dotInd + 1:]

                if len(bBeta) == 0:
                    continue

                B = bBeta[0]
                if self.__grammar.isTerminal(B):
                    continue

                prodsforB = self.__grammar.getProdForNonTerm(B)

                for p in prodsforB:
                    for t in p:
                        dottedProd = (B, ['.' + t])
                        if dottedProd not in C:
                            C += [dottedProd]
                            going = True
        return C

    def getCannonicalCollection(self):
        C = [self.closure([('S1', ['.'+ self.__grammar.getStartingSymb()])])]


