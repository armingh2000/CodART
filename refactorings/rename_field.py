from antlr4 import *
from refactorings.gen.Java9_v2Listener import Java9_v2Listener
from refactorings.gen.Java9_v2Parser import Java9_v2Parser
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class RenameFieldRefactoringListener (Java9_v2Listener):

    def __init__ (self, field_identifier : str , new_field_identifier : str, class_identifier : str = None, common_token_stream: CommonTokenStream = None):
        self.enter_class = False if class_identifier else True
        self.new_field_identifier = new_field_identifier
        self.class_identifier = class_identifier
        self.field_identifier = field_identifier

        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')


    # Enter a parse tree produced by Java9_v2Parser#normalClassDeclaration.
    def enterNormalClassDeclaration(self, ctx:Java9_v2Parser.NormalClassDeclarationContext):
        if ctx.identifier().getText() != self.class_identifier:
            return
        self.enter_class = True

    # Exit a parse tree produced by Java9_v2Parser#normalClassDeclaration.
    def exitNormalClassDeclaration(self, ctx:Java9_v2Parser.NormalClassDeclarationContext):
        if self.enter_class and self.class_identifier:
            self.enter_class = False

    # Enter a parse tree produced by Java9_v2Parser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:Java9_v2Parser.VariableDeclaratorIdContext):
        if self.enter_class:
            if ctx.identifier().getText() == self.field_identifier:
                interval = ctx.getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], text = self.new_field_identifier)

    # Exit a parse tree produced by Java9_v2Parser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:Java9_v2Parser.VariableDeclaratorIdContext):
        pass

    # Enter a parse tree produced by Java9_v2Parser#fieldAccess1.
    def enterFieldAccess1(self, ctx:Java9_v2Parser.FieldAccess1Context):
        if self.enter_class:
            if ctx.identifier().getText() == self.field_identifier:
                interval = ctx.identifier().getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], text = self.new_field_identifier)

    # Exit a parse tree produced by Java9_v2Parser#fieldAccess1.
    def exitFieldAccess1(self, ctx:Java9_v2Parser.FieldAccess1Context):
        pass


    # Enter a parse tree produced by Java9_v2Parser#fieldAccess2.
    def enterFieldAccess2(self, ctx:Java9_v2Parser.FieldAccess2Context):
        if self.enter_class:
            if ctx.identifier().getText() == self.field_identifier:
                interval = ctx.identifier().getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], text = self.new_field_identifier)

    # Exit a parse tree produced by Java9_v2Parser#fieldAccess2.
    def exitFieldAccess2(self, ctx:Java9_v2Parser.FieldAccess2Context):
        pass


    # Enter a parse tree produced by Java9_v2Parser#fieldAccess3.
    def enterFieldAccess3(self, ctx:Java9_v2Parser.FieldAccess3Context):
        if self.enter_class:
            if ctx.identifier().getText() == self.field_identifier:
                interval = ctx.identifier().getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], text = self.new_field_identifier)

    # Exit a parse tree produced by Java9_v2Parser#fieldAccess3.
    def exitFieldAccess3(self, ctx:Java9_v2Parser.FieldAccess3Context):
        pass

        # Enter a parse tree produced by Java9_v2Parser#fieldAccess_lf_primary.
    def enterFieldAccess_lf_primary(self, ctx:Java9_v2Parser.FieldAccess_lf_primaryContext):
        if self.enter_class:
            if ctx.identifier().getText() == self.field_identifier:
                interval = ctx.identifier().getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], text = self.new_field_identifier)

    # Exit a parse tree produced by Java9_v2Parser#fieldAccess_lf_primary.
    def exitFieldAccess_lf_primary(self, ctx:Java9_v2Parser.FieldAccess_lf_primaryContext):
        pass

    # Enter a parse tree produced by Java9_v2Parser#fieldAccess_lfno_primary1.
    def enterFieldAccess_lfno_primary1(self, ctx:Java9_v2Parser.FieldAccess_lfno_primary1Context):
        if self.enter_class:
            if ctx.identifier().getText() == self.field_identifier:
                interval = ctx.identifier().getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], text = self.new_field_identifier)

    # Exit a parse tree produced by Java9_v2Parser#fieldAccess_lfno_primary1.
    def exitFieldAccess_lfno_primary1(self, ctx:Java9_v2Parser.FieldAccess_lfno_primary1Context):
        pass


    # Enter a parse tree produced by Java9_v2Parser#fieldAccess_lfno_primary2.
    def enterFieldAccess_lfno_primary2(self, ctx:Java9_v2Parser.FieldAccess_lfno_primary2Context):
        if self.enter_class:
            if ctx.identifier().getText() == self.field_identifier:
                interval = ctx.identifier().getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], text = self.new_field_identifier)

    # Exit a parse tree produced by Java9_v2Parser#fieldAccess_lfno_primary2.
    def exitFieldAccess_lfno_primary2(self, ctx:Java9_v2Parser.FieldAccess_lfno_primary2Context):
        pass

