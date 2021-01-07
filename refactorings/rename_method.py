from gen.Java9_v2Lexer import  Java9_v2Lexer
from gen.Java9_v2Parser import Java9_v2Parser
from gen.Java9_v2Listener import Java9_v2Listener
from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class RenameMethodListener(Java9_v2Listener):
    def __init__(self, common_token_stream: CommonTokenStream = None, method_name : str = '', new_method_name : str = ''):
        self.token_stream = common_token_stream
        self.method_name = method_name
        self.new_method_name = new_method_name
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

    def exitMethodDeclarator(self, ctx:Java9_v2Parser.MethodDeclaratorContext):
        if(self.method_name == ctx.identifier().getText()):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex, ctx.identifier().stop.tokenIndex, self.new_method_name)

    def exitMethodInvocation1(self, ctx:Java9_v2Parser.MethodInvocation1Context):
        if(ctx.methodName().identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.methodName().identifier().start.tokenIndex,
                                                    ctx.methodName().identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation2(self, ctx:Java9_v2Parser.MethodInvocation2Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation3(self, ctx:Java9_v2Parser.MethodInvocation3Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation4(self, ctx:Java9_v2Parser.MethodInvocation4Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation5(self, ctx:Java9_v2Parser.MethodInvocation5Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation6(self, ctx:Java9_v2Parser.MethodInvocation6Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation_lf_primary(self, ctx:Java9_v2Parser.MethodInvocation_lf_primaryContext):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation_lfno_primary1(self, ctx:Java9_v2Parser.MethodInvocation_lfno_primary1Context):
        if (ctx.methodName().identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.methodName().identifier().start.tokenIndex,
                                                    ctx.methodName().identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation_lfno_primary2(self, ctx:Java9_v2Parser.MethodInvocation_lfno_primary2Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation_lfno_primary3(self, ctx:Java9_v2Parser.MethodInvocation_lfno_primary3Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation_lfno_primary4(self, ctx:Java9_v2Parser.MethodInvocation_lfno_primary4Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodInvocation_lfno_primary5(self, ctx:Java9_v2Parser.MethodInvocation_lfno_primary5Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference1(self, ctx:Java9_v2Parser.MethodReference1Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference2(self, ctx:Java9_v2Parser.MethodReference2Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference3(self, ctx:Java9_v2Parser.MethodReference3Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference4(self, ctx:Java9_v2Parser.MethodReference4Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference5(self, ctx:Java9_v2Parser.MethodReference5Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference_lf_primary(self, ctx:Java9_v2Parser.MethodReference_lf_primaryContext):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference_lfno_primary1(self, ctx:Java9_v2Parser.MethodReference_lfno_primary1Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference_lfno_primary2(self, ctx:Java9_v2Parser.MethodReference_lfno_primary2Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference_lfno_primary3(self, ctx:Java9_v2Parser.MethodReference_lfno_primary3Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
    def exitMethodReference_lfno_primary4(self, ctx:Java9_v2Parser.MethodReference_lfno_primary4Context):
        if (ctx.identifier().getText() == self.method_name):
            self.token_stream_rewriter.replaceRange(ctx.identifier().start.tokenIndex,
                                                    ctx.identifier().stop.tokenIndex,
                                                    self.new_method_name)
