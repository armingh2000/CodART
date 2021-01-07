from antlr4 import *
from gen.javaLabeled.JavaParserLabeledListener import JavaParserLabeledListener
from gen.javaLabeled.JavaParserLabeled import JavaParserLabeled
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class RenameFieldRefactoringListener (JavaParserLabeledListener):

    def __init__ (self, field_identifier : str , new_field_identifier : str, class_identifier : str = None, common_token_stream: CommonTokenStream = None):
        self.enter_class = False if class_identifier else True
        self.new_field_identifier = new_field_identifier
        self.class_identifier = class_identifier
        self.field_identifier = field_identifier

        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

    # Enter a parse tree produced by JavaParserLabeled#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaParserLabeled.ClassDeclarationContext):
        if ctx.IDENTIFIER().getText() != self.class_identifier:
            return
        self.enter_class = True

    # Exit a parse tree produced by JavaParserLabeled#classDeclaration.
    def exitClassDeclaration(self, ctx:JavaParserLabeled.ClassDeclarationContext):
        if self.enter_class and self.class_identifier:
            self.enter_class = False

    # Enter a parse tree produced by JavaParserLabeled#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:JavaParserLabeled.VariableDeclaratorIdContext):
        if self.enter_class:
            if ctx.IDENTIFIER().getText() == self.field_identifier:
                interval = ctx.getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], text = self.new_field_identifier)

    # Exit a parse tree produced by JavaParserLabeled#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:JavaParserLabeled.VariableDeclaratorIdContext):
        pass

    # Enter a parse tree produced by JavaParserLabeled#expression1.
    def enterExpression1(self, ctx:JavaParserLabeled.Expression1Context):
        if self.enter_class:
            if ctx.IDENTIFIER().getText() == self.field_identifier:
                interval = ctx.IDENTIFIER().getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], text = self.new_field_identifier)

    # Exit a parse tree produced by JavaParserLabeled#expression1.
    def exitExpression1(self, ctx:JavaParserLabeled.Expression1Context):
        pass

