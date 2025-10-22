from django.shortcuts import render
from antlr4 import InputStream, CommonTokenStream
from antlr.ExamenLexer import ExamenLexer
from antlr.ExamenParser import ExamenParser
from antlr.EvalExamVisitor import EvalExamVisitor

def evaluate_expression_text(expr_text: str):
    input_stream = InputStream(expr_text)
    lexer = ExamenLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ExamenParser(token_stream)
    tree = parser.expr()
    evaluator = EvalExamVisitor()
    result = evaluator.visit(tree)
    return result

def index(request):
    result = None
    if request.method == "POST":
        try:
            x = int(request.POST.get('x'))
            y = int(request.POST.get('y'))
            z = x * y + 10
            x_after = x + 1
            result = f"{x} * {y} + 10 = {z}<br>{x} + 1 = {x_after}"
        except Exception as e:
            result = f"Error: {e}"
    return render(request, 'examapp/index.html', {'result': result})