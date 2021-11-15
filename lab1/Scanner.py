import re

from SymbolTable import *



class Scanner:
    def __init__(self, filename):
        self.__filename = filename
        self.__tokens = {}
        self.__PIF = {}
        self.__PIF2 = []
        self.__PIF[0] = []
        self.__PIF[1] = []
        self.__error = {}
        self.__ST = SymbolTable()
        self.__reserved_words = ["int", "char", "float", "bool", "const", "if", "then", "else", "begin", "end", "read", "write",
                                 "while","do", "end-while", "break", "true", "false", "array", "sqrt"]
        self.__delimiters = ";", ",", "{", "}", "(", ")", ":", "*", "/", "<", ">", "and","or", "!=", "==", "<=",\
                            ">=", "=", " ", "do", "end-while"
        self._constants =[]
        self._identifiers = []

        self.generate_codes()

    def generate_codes(self):
        file = open("token.txt", 'r')
        line = file.readline().strip("\n")
        while line != "":
            codes = line.split(",")
            self.__tokens[codes[0]] = int(codes[1])
            line = file.readline().strip("\n")

    def get_PIF(self):
        return self.__PIF

    def get_PIF2(self):
        return self.__PIF2


    def isIdentifier(self, token):
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_)*$', token) is not None

    def isConstant(self, token):
        return re.match('^(0|[\+\-]?[1-9][0-9]*)$', token) is not None

    def is_reserverd_word(self, word):
        if word in self.__reserved_words:
            return True
        return False


    def get_error(self):
        return self.__error

    def construct_pif2(self):
        print(self.__ST)

        file = open(self.__filename, 'r')
        line = file.readline().strip("\n")
        self.__delimiters = ";", ",", "{", "}", "(", ")", ":", "*", "/", "<", ">", "and", "or", "!=", "==", "<=", \
                            ">=", "=", " "
        while line != "":
            regexPattern = '|'.join(map(re.escape, " "))
            tokens = re.split(regexPattern, line)

            for i in range(0, len(tokens)):
                if tokens[i] is not None and len(tokens[i]) > 0:
                    if tokens[i] in self.__tokens.keys():
                        self.__PIF[self.__tokens.get(tokens[i])] = -1
                        string = str(tokens[i]) + " " + str(self.__tokens.get(tokens[i])) + " " + "-1"
                        self.__PIF2.append(string)
                    elif self.isIdentifier(tokens[i]):
                        self.__PIF[0].append(self.__ST.get(tokens[i]))
                        string = str(tokens[i]) + " " + str(self.__ST.get(tokens[i])) + " " + "0"
                        self.__PIF2.append(string)
                    elif self.isConstant(tokens[i]):
                        self.__PIF[1].append(self.__ST.get(tokens[i]))
                        string = str(tokens[i]) + " " + str(self.__ST.get(tokens[i])) + " " + "1"
                        self.__PIF2.append(string)

            line = file.readline().strip("\n")
        file.close()


    def construct_pif(self):
        print(self.__ST)

        file = open(self.__filename, 'r')
        line = file.readline().strip("\n")
        delimiters = ";", ",", "{", "}", "(", ")", ":", "*", "/", "<", ">", "and", "or", "!=", "==", "<=", \
                     ">=", "=", "[", "]", " ", "do", "end-while"
        while line != "":
            regexPattern = '|'.join(map(re.escape, delimiters))
            tokens = re.split(regexPattern, line)



            for i in range(0, len(tokens)):
                if tokens[i] is not None and len(tokens[i]) > 0:
                    if tokens[i] in self.__tokens.keys():
                        self.__PIF[self.__tokens.get(tokens[i])] = -1
                    elif self.isIdentifier(tokens[i]):
                        self.__PIF[0].append(self.__ST.get(tokens[i]))
                    elif self.isConstant(tokens[i]):
                        self.__PIF[1].append( self.__ST.get(tokens[i]))


            line = file.readline().strip("\n")
        file.close()


    def tokenize(self):
        file = open(self.__filename, 'r')
        line = file.readline().strip("\n")
        count_line = 1
        first = True
        while line != "" and len(self.__error) == 0:
            regexPattern = '|'.join(map(re.escape, self.__delimiters))
            tokens = re.split(regexPattern, line)

            for element in tokens:
                if element == '':
                    tokens.remove(element)


            if len(self.__error) == 0:
                for i in range(len(tokens)):
                    current_error = ""
                    found = False


                    if tokens[i] is not None and len(tokens[i]) > 0  and len(
                            list(tokens[i])) > 0 and tokens[i] not in ['+', '-']:
                        if self.is_reserverd_word(tokens[i]):
                            current_error = ""
                        else:
                            if not self.isIdentifier(tokens[i]):
                                current_error = "lexical error " + tokens[i]
                                if tokens[i][0] == '-':
                                    l = list(tokens[i])
                                    ident = l[1:]
                                    if self.isIdentifier(ident[0]):
                                        current_error = ""
                                        found = True
                            else:
                                found = True
                                self.__ST.add(tokens[i])
                            if not self.isConstant(tokens[i]):
                                if not found:
                                    current_error = "lexical error "  + tokens[i]
                            else:
                                current_error = ""
                                self.__ST.add(tokens[i])

                            if '[' in list(tokens[i]) and ']' in list(tokens[i]):
                                arr = tokens[i].split('[')
                                splitted = arr[1].split(']')

                                if self.isConstant(splitted[0]) or self.isIdentifier(splitted[0]):
                                    self.__ST.add(splitted[0])
                                    current_error = ""

                        if current_error != "":
                            err = ""
                            err += current_error + " at line "
                            self.__error[err] = count_line
                            break


            count_line += 1
            line = file.readline().strip("\n")

        file.close()
        if len(self.__error) > 0:
            file_st = open("st.txt", 'w')
            file_st.write("")
            file_st.close()
            self.construct_pif()
            return True
        else:
            return False






