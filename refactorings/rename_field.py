
__author__  = 'Armin Gholampoor (@github:armingh2000)'
from antlr4 import *
from gen.javaLabeled.JavaParserLabeledListener import JavaParserLabeledListener
from gen.javaLabeled.JavaParserLabeled import JavaParserLabeled
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class RenameFieldRefactoringListener (JavaParserLabeledListener):
    def __init__ (self, field_identifier : str , new_field_identifier : str, class_identifier : str, common_token_stream: CommonTokenStream = None):
        self.isRelevant = False
        self.new_field_identifier = new_field_identifier
        self.class_identifier = class_identifier
        self.field_identifier = field_identifier
        self.class_holder = dict()

        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

    # Exit a parse tree produced by JavaParserLabeled#classDeclaration.
    def enterClassDeclaration(self, ctx:JavaParserLabeled.ClassDeclarationContext):
        if ctx.IDENTIFIER().getText() == self.class_identifier:
            self.isRelevant = True

    # Exit a parse tree produced by JavaParserLabeled#classDeclaration.
    def exitClassDeclaration(self, ctx:JavaParserLabeled.ClassDeclarationContext):
        self.isRelevant = False

    # Exit a parse tree produced by JavaParserLabeled#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:JavaParserLabeled.FieldDeclarationContext):
        if self.isRelevant:
            vds = ctx.children[1]
            for child in vds.children:
                text = child.getText()
                if text == self.field_identifier:
                    identifier = child.variableDeclaratorId().IDENTIFIER()
                    if identifier.getText() == self.field_identifier:
                        interval = identifier.getSourceInterval()
                        self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_field_identifier)

    # Exit a parse tree produced by JavaParserLabeled#variableDeclarator.
    def exitVariableDeclarator(self, ctx:JavaParserLabeled.VariableDeclaratorContext):
        self.class_holder[ctx.variableDeclaratorId().IDENTIFIER().getText()] = ctx.parentCtx.parentCtx.typeType().getText()

    # Exit a parse tree produced by JavaParserLabeled#primary4.
    def exitPrimary4(self, ctx:JavaParserLabeled.Primary4Context):
        if self.isRelevant:
            identifier = ctx.IDENTIFIER()
            if identifier.getText() == self.field_identifier:
                interval = identifier.getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_field_identifier)

        if ctx.getText() in self.class_holder.keys() and self.class_holder[ctx.getText()] == self.class_identifier:
            child = ctx.parentCtx.parentCtx.children[2]
            if child.getText() == self.field_identifier:
                identifier = child
                interval = identifier.getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_field_identifier)

    # Exit a parse tree produced by JavaParserLabeled#primary1.
    def exitPrimary1(self, ctx:JavaParserLabeled.Primary1Context):
        if self.isRelevant:
            if ctx.getText() == "this":
                exp = ctx.parentCtx.parentCtx
                identifier = exp.IDENTIFIER()
                if identifier.getText() == self.field_identifier:
                    interval = identifier.getSourceInterval()
                    self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_field_identifier)

    # Exit a parse tree produced by JavaParserLabeled#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:JavaParserLabeled.ClassOrInterfaceTypeContext):
        if self.isRelevant:
            for child in ctx.children:
                text = child.getText()
                if text == self.field_identifier:
                    identifier = ctx.IDENTIFIER()
                    if identifier.getText() == self.field_identifier:
                        interval = identifier.getSourceInterval
                        self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_field_identifier)
