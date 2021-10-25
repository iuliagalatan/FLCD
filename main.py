
from Scanner import *

'''
symbolTable = SymbolTable()

symbolTable.add("z")
symbolTable.add("a")
symbolTable.add("d")
symbolTable.add("ab")
symbolTable.add("ab")



print(symbolTable.get("a"))
print(symbolTable.get("d"))
print(symbolTable.get("z"))
print(symbolTable.get("q"))
print(symbolTable.get("ab"))


print(symbolTable)
'''
scaner = Scanner("p3.txt")
error = scaner.tokenize()
if not error:

    scaner.construct_pif2()
    print(scaner.get_PIF())
    print(scaner.get_PIF2())
    file = open("pif.txt", 'w')
    file.write(str(scaner.get_PIF()))
    file.close()
else:
    print(str(scaner.get_error()))
