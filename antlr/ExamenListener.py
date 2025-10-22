# Generated from Examen.g by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExamenParser import ExamenParser
else:
    from ExamenParser import ExamenParser

# This class defines a complete listener for a parse tree produced by ExamenParser.
class ExamenListener(ParseTreeListener):

    # Enter a parse tree produced by ExamenParser#program.
    def enterProgram(self, ctx:ExamenParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExamenParser#program.
    def exitProgram(self, ctx:ExamenParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExamenParser#statement.
    def enterStatement(self, ctx:ExamenParser.StatementContext):
        pass

    # Exit a parse tree produced by ExamenParser#statement.
    def exitStatement(self, ctx:ExamenParser.StatementContext):
        pass


    # Enter a parse tree produced by ExamenParser#assign.
    def enterAssign(self, ctx:ExamenParser.AssignContext):
        pass

    # Exit a parse tree produced by ExamenParser#assign.
    def exitAssign(self, ctx:ExamenParser.AssignContext):
        pass


    # Enter a parse tree produced by ExamenParser#print.
    def enterPrint(self, ctx:ExamenParser.PrintContext):
        pass

    # Exit a parse tree produced by ExamenParser#print.
    def exitPrint(self, ctx:ExamenParser.PrintContext):
        pass


    # Enter a parse tree produced by ExamenParser#expr.
    def enterExpr(self, ctx:ExamenParser.ExprContext):
        pass

    # Exit a parse tree produced by ExamenParser#expr.
    def exitExpr(self, ctx:ExamenParser.ExprContext):
        pass



del ExamenParser