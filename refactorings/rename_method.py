from gen.javaLabeled.JavaLexer import  JavaLexer
from gen.javaLabeled.JavaParserLabeledListener import JavaParserLabeledListener
from gen.javaLabeled.JavaParserLabeled import JavaParserLabeled
from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class RenameMethodListener(JavaParserLabeledListener):
    def __init__(self, common_token_stream: CommonTokenStream = None, class_identifier : str =None, method_name : str = '', new_method_name : str = ''):
        self.enter_class = False if class_identifier else True
        self.token_stream = common_token_stream
        self.method_name = method_name
        self.new_method_name = new_method_name
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        if ctx.IDENTIFIER().getText() != self.class_identifier:
            return
        self.enter_class = True

    def exitClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        if self.enter_class and self.class_identifier:
            self.enter_class = False

    def exitMethodDeclaration(self, ctx:JavaParserLabeled.MethodDeclarationContext):
        if(not self.enter_class):
            return
        if(self.method_name == ctx.IDENTIFIER().getText()):
            interval = ctx.IDENTIFIER().getSourceInterval()
            self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_method_name)
    def exitInterfaceMethodDeclaration(self, ctx:JavaParserLabeled.InterfaceMethodDeclarationContext):
        if (not self.enter_class):
            return
        if (self.method_name == ctx.IDENTIFIER().getText()):
            interval = ctx.IDENTIFIER().getSourceInterval()
            self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_method_name)
    def exitAnnotationMethodRest(self, ctx:JavaParserLabeled.AnnotationMethodRestContext):
        if(ctx.IDENTIFIER().getText() == self.method_name):
            interval = ctx.IDENTIFIER().getSourceInterval()
            self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_method_name)
    def exitMethodCall0(self, ctx:JavaParserLabeled.MethodCall0Context):
        if (ctx.IDENTIFIER().getText() == self.method_name):
            interval = ctx.IDENTIFIER().getSourceInterval()
            self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_method_name)
    def exitexpression23(self, ctx:JavaParserLabeled.Expression23Context):
        print("Yo!")
        if (ctx.IDENTIFIER().getText() == self.method_name):
            interval = ctx.IDENTIFIER().getSourceInterval()
            self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_method_name)
    def exitexpression24(self, ctx:JavaParserLabeled.Expression24Context):
        print("Yo!")
        if (ctx.IDENTIFIER().getText() == self.method_name):
            interval = ctx.IDENTIFIER().getSourceInterval()
            self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_method_name)
