from SortedList import SortedList


class SymbolTable:
    def __init__(self):
        self.__sortedList = SortedList()

    def add(self, value):
        return self.__sortedList.insert(value)

    def get(self, value):
        return self.__sortedList.binary_search(value)

    def __str__(self):
        return str(self.__sortedList)