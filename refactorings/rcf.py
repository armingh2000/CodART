
__author__  = 'Armin Gholampoor (@github:armingh2000) - Hadi Sheikhi (@github:...)'
#hadi age khasti username githubeto bezan bala
from antlr4 import *
from gen.javaLabeled.JavaParserLabeledListener import JavaParserLabeledListener
from gen.javaLabeled.JavaParserLabeled import JavaParserLabeled
from antlr4.TokenStreamRewriter import TokenStreamRewriter

class RemoveControlFlagRefactoringListener (JavaParserLabeledListener):
    def __init__ (self, common_token_stream: CommonTokenStream = None):
        self.isRelevant = False
        self.relevantVariable = None
        self.ifStmnt = None
        self.relevantVariableValue = None
        self.lastOccurance = dict()
        self.hasBlock = False
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

    # Enter a parse tree produced by JavaParserLabeled#statement3.
    def enterStatement3(self, ctx:JavaParserLabeled.Statement3Context):
        if isinstance(ctx.statement(), JavaParserLabeled.Statement0Context):
            self.ifStmnt = ctx.statement().block().blockStatement(0).statement()
            self.hasBlock = True
            if isinstance(self.ifStmnt, JavaParserLabeled.Statement2Context):
                exp = self.ifStmnt.parExpression().expression()
                if isinstance(exp, JavaParserLabeled.Expression0Context):
                    prm = exp.primary()
                    if isinstance(prm, JavaParserLabeled.Primary4Context):
                        self.isRelevant += 1
                        self.relevantVariable = prm.IDENTIFIER().getText()


                elif isinstance(exp, JavaParserLabeled.Expression8Context):
                    exp2 = exp.expression()
                    if isinstance(exp2, JavaParserLabeled.Expression0Context):
                        prm = exp2.primary()
                        if isinstance(prm, JavaParserLabeled.Primary4Context):
                            self.isRelevant += 1
                            self.relevantVariable = prm.IDENTIFIER().getText()


        elif isinstance(ctx.statement(), JavaParserLabeled.Statement2Context):
            self.ifStmnt = ctx.statement()
            exp = self.ifStmnt.parExpression().expression()
            if isinstance(exp, JavaParserLabeled.Expression0Context):
                prm = exp.primary()
                if isinstance(prm, JavaParserLabeled.Primary4Context):
                    self.isRelevant += 1
                    self.relevantVariable = prm.IDENTIFIER().getText()


            elif isinstance(exp, JavaParserLabeled.Expression8Context):
                exp2 = exp.expression()
                if isinstance(exp2, JavaParserLabeled.Expression0Context):
                    prm = exp2.primary()
                    if isinstance(prm, JavaParserLabeled.Primary4Context):
                        self.isRelevant += 1
                        self.relevantVariable = prm.IDENTIFIER().getText()

    # Exit a parse tree produced by JavaParserLabeled#statement3.
    def exitStatement3(self, ctx:JavaParserLabeled.Statement3Context):
        if self.isRelevant:
            if(not self.hasBlock):
                interval = self.ifStmnt.getSourceInterval()
                stmnt = self.ifStmnt.statement(0)
                interval2 = stmnt.getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.token_stream_rewriter.getText('default', interval2[0] , interval2[1]))
                declarationInterval = self.lastOccurance[self.relevantVariable].getSourceInterval()
                self.token_stream_rewriter.replaceRange(declarationInterval[0], declarationInterval[1], "")
            else:
                interval = self.ifStmnt.parentCtx.parentCtx.getSourceInterval()
                stmnt = self.ifStmnt.statement(0)
                interval2 = stmnt.getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.token_stream_rewriter.getText('default', interval2[0], interval2[1]))
                declarationInterval = self.lastOccurance[self.relevantVariable].getSourceInterval()
                self.token_stream_rewriter.replaceRange(declarationInterval[0], declarationInterval[1], "")
        self.isRelevant -= 1


    # Enter a parse tree produced by JavaParserLabeled#statement4.
    def enterStatement4(self, ctx:JavaParserLabeled.Statement4Context):
        if isinstance(ctx.statement(), JavaParserLabeled.Statement0Context):
            self.ifStmnt = ctx.statement().block().blockStatement(0).statement()
            if isinstance(self.ifStmnt, JavaParserLabeled.Statement2Context):
                exp = self.ifStmnt.parExpression().expression()
                if isinstance(exp, JavaParserLabeled.Expression0Context):
                    prm = exp.primary()
                    if isinstance(prm, JavaParserLabeled.Primary4Context):
                        self.isRelevant += 1
                        self.relevantVariable = prm.IDENTIFIER().getText()


                elif isinstance(exp, JavaParserLabeled.Expression8Context):
                    exp2 = exp.expression()
                    if isinstance(exp2, JavaParserLabeled.Expression0Context):
                        prm = exp2.primary()
                        if isinstance(prm, JavaParserLabeled.Primary4Context):
                            self.isRelevant += 1
                            self.relevantVariable = prm.IDENTIFIER().getText()


        elif isinstance(ctx.statement(), JavaParserLabeled.Statement2Context):
            self.ifStmnt = ctx
            exp = self.ifStmnt.parExpression().expression()
            if isinstance(exp, JavaParserLabeled.Expression0Context):
                prm = exp.primary()
                if isinstance(prm, JavaParserLabeled.Primary4Context):
                    self.isRelevant += 1
                    self.relevantVariable = prm.IDENTIFIER().getText()


            elif isinstance(exp, JavaParserLabeled.Expression8Context):
                exp2 = exp.expression()
                if isinstance(exp2, JavaParserLabeled.Expression0Context):
                    prm = exp2.primary()
                    if isinstance(prm, JavaParserLabeled.Primary4Context):
                        self.isRelevant += 1
                        self.relevantVariable = prm.IDENTIFIER().getText()


    # Exit a parse tree produced by JavaParserLabeled#statement4.
    def exitStatement4(self, ctx:JavaParserLabeled.Statement4Context):
        if self.isRelevant:
            interval = self.ifStmnt.parentCtx.parentCtx.getSourceInterval()
            stmnt = self.ifStmnt.statement(0)
            interval2 = stmnt.getSourceInterval()
            self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.token_stream_rewriter.getText('default', interval2[0], interval2[1]))
            declarationInterval = self.lastOccurance[self.relevantVariable].getSourceInterval()
            self.token_stream_rewriter.replaceRange(declarationInterval[0], declarationInterval[1], "")
        self.isRelevant -= 1

     # Enter a parse tree produced by JavaParserLabeled#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:JavaParserLabeled.LocalVariableDeclarationContext):
        if self.isRelevant:
            pass

        else:
            for child in ctx.variableDeclarators().variableDeclarator():
                self.lastOccurance[child.variableDeclaratorId().getText()] = ctx.parentCtx
                self.relevantVariableValue = child.variableInitializer().getText()

    # Exit a parse tree produced by JavaParserLabeled#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:JavaParserLabeled.LocalVariableDeclarationContext):
        pass

    # Enter a parse tree produced by JavaParserLabeled#expression1.
    def enterExpression21(self, ctx:JavaParserLabeled.Expression21Context):
        if self.isRelevant:
            if ctx.expression(0).getText() == self.relevantVariable:
                interval = ctx.getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], "break")


    # Exit a parse tree produced by JavaParserLabeled#expression1.
    def exitExpression21(self, ctx:JavaParserLabeled.Expression21Context):
        pass
