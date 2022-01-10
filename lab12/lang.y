%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
int yyerror(char *s);
extern FILE *yyin;
extern int yylineno;
%}

%token IDENTIFIER
%token CONSTANT
%token STRING
%token INT
%token BOOL
%token CHAR
%token FLOAT
%token CONST
%token IF
%token WHILE
%token ELSE
%token BEGIN
%token END
%token READ
%token WRITE
%token BREAK
%token COLON
%token SEMI_COLON
%token COMA
%token DOT
%token PLUS
%token MINUS
%token MULTIPLY
%token DIVISION
%token LEFT_ROUND_PARENTHESIS
%token RIGHT_ROUND_PARENTHESIS
%token LEFT_SQUARE_PARENTHESIS
%token RIGHT_SQUARE_PARENTHESIS
%token LESS_THAN
%token GREATER_THAN
%token LESS_OR_EQUAL_THAN
%token GREATER_OR_EQUAL_THAN
%token DIFFERENT
%token EQUAL
%token ASSIGNMENT
%token OR
%token AND
%token LEFT_CURLY_BRACKET
%token RIGHT_CURLY_BRACKET

%start program

%%

program : declist cmpdstmt
declist : declaration | declaration declist
declaration: type identifierList SEMI_COLON | arraydecl SEMI_COLON
identifierList : IDENTIFIER | IDENTIFIER COMA identifierList
type   : INT | BOOL | CHAR | FLOAT
arraydecl : type IDENTIFIER LEFT_SQUARE_PARENTHESIS CONSTANT RIGHT_SQUARE_PARENTHESIS
cmpdstmt : stmt | stmt cmpdstmt
stmt    : simplstmt SEMI_COLON | structstmt
simplstmt : assignstmt | iostmt
assignstmt : IDENTIFIER ASSIGNMENT expression
iostmt  : WRITE IDENTIFIER | READ IDENTIFIER | WRITE CONSTANT | WRITE WORD 
expression : expression PLUS term | expression MINUS term | expression MULTIPLY term  | expression DIVISION term | term
term : IDENTIFIER | CONSTANT | arrElem
arrElem : IDENTIFIER LEFT_SQUARE_PARENTHESIS CONST RIGHT_SQUARE_PARENTHESIS | IDENTIFIER LEFT_SQUARE_PARENTHESIS IDENTIFIER RIGHT_SQUARE_PARENTHESIS
structstmt : whilestmt | ifstmt
whilestmt : WHILE LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS stmt
condition : expression relation expression
relation  : LESS_THAN | LESS_OR_EQUAL_THAN | GREATER_THAN | GREATER_OR_EQUAL_THAN | EQUAL | DIFFERENT | AND | OR
ifstmt : IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS stmt ELSE stmt | IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS stmt

%%
int yyerror(char *s)
{
	printf("%s on line %d\n", s, yylineno);
	return 0;
}

int main(int argc, char** argv)
{
    if (argc == 2) {
        yyin = fopen(argv[1], "r");
        yyparse();
    }
    yyparse();
    printf("Done");
    return 0;
}