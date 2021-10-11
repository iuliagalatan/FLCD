from SymbolTable import *

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