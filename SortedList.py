from bisect import *
class SortedList:
    def __init__(self):
        self.__sortedList = []
        self.__cnt = 0

    def insert(self, value):
        id = self.search(value)
        if id != False:
            return id
        self.__sortedList.append((value, self.__cnt))
        self.__cnt += 1
        self.__sortedList = sorted(self.__sortedList, key=lambda x: x[0])
        return self.__cnt - 1

    def search(self, value):
        for i in self.__sortedList:
            if i[0] == value:
                return i[1]
        return False

    def binary_search(self, value):
        i = bisect_left(self.__sortedList, value)
        if i != len(self.__sortedList) and self.__sortedList[i][0] == value:
            return self.__sortedList[i][1]
        else:
            return -1

    def __str__(self):
        return str(self.__sortedList)