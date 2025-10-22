# Generated from Examen.g by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExamenParser import ExamenParser
else:
    from ExamenParser import ExamenParser

# This class defines a complete generic visitor for a parse tree produced by ExamenParser.

class ExamenVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExamenParser#program.
    def visitProgram(self, ctx:ExamenParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExamenParser#statement.
    def visitStatement(self, ctx:ExamenParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExamenParser#assign.
    def visitAssign(self, ctx:ExamenParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExamenParser#print.
    def visitPrint(self, ctx:ExamenParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExamenParser#expr.
    def visitExpr(self, ctx:ExamenParser.ExprContext):
        return self.visitChildren(ctx)



del ExamenParser