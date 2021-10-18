import re

from SymbolTable import *
from main import symbolTable


class Scanner:
    def __init__(self, filename):
        self.__filename = filename
        self.__tokens = {}
        self.__PIF = {}
        self.__error = {}
        self.__ST = symbolTable()
        self.__reserved_words = ["int", "char", "float", "bool", "const", "if", "then", "else", "begin", "end", "read", "write",
                                 "while","do", "end-while", "break", "true", "false", "array"]
        self.__delimiters = ";", ",", "{", "}", "(", ")", ":", "*", "/", "<", ">", "and","or", "!=", "==", "<=",\
                            ">=", "=", " ", "do", "end-while"

        self.generate_codes()

    def generate_codes(self):
        file = open("token.txt", 'r')
        line = file.readline().strip("\n")
        while line != "":
            codes = line.split(",")
            self.__tokens[codes[0]] = int(codes[1])
            line = file.readline().strip("\n")

    def isIdentifier(self, token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_)*$', token) is not None

    def isConstant(self, token):
        return re.match('^(0|[\+\-]?[1-9][0-9]*)$', token) is not None

    def is_reserverd_word(self, word):
        if word in self.__reserved_words:
            return True
        return False

    def tokenize(self):
        file = open(self.__filename, 'r')
        line = file.readline().strip("\n")
        count_line = 1
        first = True
        while line != "" and len(self.__error) == 0:
            regexPattern = '|'.join(map(re.escape, self.__delimiters))
            tokens = re.split(regexPattern, line)



            if tokens[0] != None:
                if tokens[0] != "then" or tokens[0] != "do":
                    if len(tokens[0]) > 0 and len(self.__error) == 0:
                        if tokens[0] not in self.__tokens.keys() and not self.isIdentifier(tokens[0]) and not self.is_reserverd_word(tokens[0]):
                            self.__error["Invalid identifier at line"] = count_line
                            break
            if len(self.__error) == 0:
                for i in range(len(tokens)):
                    current_error = ""
                    found = False
                    if tokens[i] is not None and len(tokens[i]) > 0  and len(
                            list(tokens[i])) > 0 and tokens[i] not in ['+', '-']:
                        if not self.isIdentifier(tokens[i]):
                            current_error = "invalid identifier"
                        else:
                            found = True
                            self.__ST.add(tokens[i])
                        if not self.isConstant(tokens[i]):
                            if not found:
                                current_error = "invalid constant"
                        else:
                            current_error = ""
                        if self.is_reserverd_word(tokens[i]):
                            current_error = ""
                        if '[' in list(tokens[i]) and ']' in list(tokens[i]):
                            arr = tokens[i].split('[')
                            if arr[0] != "array":
                                current_error ="invalid array declaration"
                                splitted = arr[1].split(']')
                                if self.isConstant(splitted[0]):
                                    current_error = ""
                        if current_error != "":
                            err = ""
                            err += current_error + " at line "
                            self.__error[err] = count_line
                            break

            count_line += 1
            line = file.readline().strip("\n")

        file.close()






