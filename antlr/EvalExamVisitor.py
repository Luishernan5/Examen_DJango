from antlr.ExamenVisitor import ExamenVisitor  # generado por ANTLR
from antlr.ExamenParser import ExamenParser
from antlr.ExamenLexer import ExamenLexer

class EvalExamVisitor(ExamenVisitor):
    def _init_(self):
        super()._init_()
        self.memory = {}

    def visitAssign(self, ctx:ExamenParser.AssignContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[var_name] = value
        return value

    def visitPrint(self, ctx:ExamenParser.PrintContext):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitMulDiv(self, ctx:ExamenParser.ExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return left * right
        else:
            if right == 0:
                raise ValueError("División por cero")
            return left / right

    def visitAddSub(self, ctx:ExamenParser.ExprContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitInt(self, ctx:ExamenParser.ExprContext):
        return int(ctx.INT().getText())

    def visitVariable(self, ctx:ExamenParser.ExprContext):
        var_name = ctx.ID().getText()
        if var_name not in self.memory:
            raise NameError(f"Variable '{var_name}' no definida")
        return self.memory[var_name]