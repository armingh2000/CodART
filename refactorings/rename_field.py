
__author__  = 'Armin Gholampoor (@github:armingh2000)'
from antlr4 import *
from gen.javaLabeled.JavaParserLabeledListener import JavaParserLabeledListener
from gen.javaLabeled.JavaParserLabeled import JavaParserLabeled
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from gen.javaLabeled.JavaLexer import  JavaLexer


class RenameFieldRefactoringListener (JavaParserLabeledListener):
    def __init__ (self, field_identifier : str ,
                  new_field_identifier : str,
                  class_identifier : str,
                  common_token_stream: CommonTokenStream = None,
                  extentions=[],
                  implementations=[]):
        self.enter_class = False
        self.new_field_identifier = new_field_identifier
        self.class_identifier = class_identifier
        self.field_identifier = field_identifier

        self.scope_handler = ScopeHandler()
        self.symbol_table = SymbolTable()
        self.last_used_type = None
        self.extentions = extentions
        self.implementations = implementations

        self.seen_classes = []

        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')



    def exitPrimitiveType(self, ctx:JavaParserLabeled.PrimitiveTypeContext):
        self.last_used_type = ctx.getText()

    def exitClassOrInterfaceType(self, ctx:JavaParserLabeled.ClassOrInterfaceTypeContext):
        self.last_used_type = ctx.IDENTIFIER()[-1].getText()

    def enterLocalVariableDeclaration(self, ctx:JavaParserLabeled.LocalVariableDeclarationContext):
        self.scope_handler.enterVariableDeclaration()
    def exitLocalVariableDeclaration(self, ctx:JavaParserLabeled.LocalVariableDeclarationContext):
        self.scope_handler.exitVariableDeclaration()
    def exitVariableDeclaratorId(self, ctx:JavaParserLabeled.VariableDeclaratorIdContext):
        self.symbol_table.Insert(self.scope_handler.getScope(), ctx.IDENTIFIER().getText(), self.last_used_type)


    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        id = ctx.IDENTIFIER().getText()
        self.scope_handler.enterClass(id)
        self.symbol_table.AddnewClass(id)
        self.enter_class = id == self.class_identifier
        self.seen_classes.append(ctx.IDENTIFIER().getText())
        if(id in self.extentions or id in self.implementations):
            self.enter_class = True

    def exitClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self.seen_classes.pop()
        self.scope_handler.exitClass(ctx.IDENTIFIER().getText())
        id = ctx.IDENTIFIER().getText()
        if (id == self.class_identifier):
            self.enter_class = False
        else:
            try:
                self.enter_class = self.seen_classes[-1] == self.class_identifier
            except:
                pass

    def enterInterfaceDeclaration(self, ctx:JavaParserLabeled.InterfaceDeclarationContext):
        self.seen_classes.append(ctx.IDENTIFIER().getText())
        self.scope_handler.enterClass(ctx.IDENTIFIER().getText())
        self.symbol_table.AddnewClass(ctx.IDENTIFIER().getText())
        self.enter_class = ctx.IDENTIFIER().getText() == self.class_identifier

    def exitInterfaceDeclaration(self, ctx:JavaParserLabeled.InterfaceDeclarationContext):
        self.seen_classes.pop()
        if (id == self.class_identifier):
            self.enter_class = False

        else:
            try:
                self.enter_class = self.seen_classes[-1] == self.class_identifier
            except:
                pass
        self.scope_handler.exitClass(ctx.IDENTIFIER().getText())

    def enterMethodDeclaration(self, ctx:JavaParserLabeled.MethodDeclarationContext):
        self.scope_handler.enterMethod(ctx.IDENTIFIER().getText())

    def enterConstructorDeclaration(self, ctx:JavaParserLabeled.ConstructorDeclarationContext):
        self.scope_handler.enterMethod(ctx.IDENTIFIER().getText())

    def exitConstructorDeclaration(self, ctx:JavaParserLabeled.ConstructorDeclarationContext):
        self.scope_handler.exitMethod(ctx.IDENTIFIER().getText())

    def enterBlock(self, ctx:JavaParserLabeled.BlockContext):
        self.scope_handler.enterBlock()

    def exitBlock(self, ctx:JavaParserLabeled.BlockContext):
        self.scope_handler.exitBlock()

    def enterSwitchBlockStatementGroup(self, ctx:JavaParserLabeled.SwitchBlockStatementGroupContext):
        self.scope_handler.enterBlock()

    def exitSwitchBlockStatementGroup(self, ctx:JavaParserLabeled.SwitchBlockStatementGroupContext):
        self.scope_handler.exitBlock()

    def enterLambdaExpression(self, ctx:JavaParserLabeled.LambdaExpressionContext):
        self.scope_handler.enterBlock()

    def exitLambdaExpression(self, ctx:JavaParserLabeled.LambdaExpressionContext):
        self.scope_handler.exitBlock()

    def enterStatement3(self, ctx:JavaParserLabeled.Statement3Context):
        self.scope_handler.enterBlock()

    def exitStatement3(self, ctx:JavaParserLabeled.Statement3Context):
        self.scope_handler.exitBlock()

    def exitMethodDeclaration(self, ctx:JavaParserLabeled.MethodDeclarationContext):
        self.scope_handler.exitMethod(ctx.IDENTIFIER().getText())

    # Exit a parse tree produced by JavaParserLabeled#expression1.
    def exitExpression1(self, ctx:JavaParserLabeled.Expression1Context):
        if self.symbol_table.FindVariableType(self.scope_handler.getScope(), ctx.expression().getText()) == self.class_identifier:

            if ctx.children[-1].getText() == self.field_identifier:
                interval = ctx.IDENTIFIER().getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_field_identifier)

        elif self.enter_class:
            if ctx.expression().getText() == "this" and ctx.children[-1].getText() == self.field_identifier:
                interval = ctx.IDENTIFIER().getSourceInterval()
                self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_field_identifier)

    # Exit a parse tree produced by JavaParserLabeled#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:JavaParserLabeled.FieldDeclarationContext):
        last_scope = self.scope_handler.getScope()[-1]
        if last_scope == self.class_identifier:
            for variableDeclarator in ctx.variableDeclarators().variableDeclarator():
                if variableDeclarator.variableDeclaratorId().getText() == self.field_identifier:
                    interval = variableDeclarator.variableDeclaratorId().IDENTIFIER().getSourceInterval()
                    self.token_stream_rewriter.replaceRange(interval[0], interval[1], self.new_field_identifier)



class ImplementaionIdentificationListener(JavaParserLabeledListener):
    def __init__(self, identifier):
        self.__class_identifier = identifier
        self.extensions = []
        self.implementations = []
    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        if(ctx.EXTENDS() is not None):
            if(ctx.IDENTIFIER().getText() not in self.extensions and ctx.typeType().getText() == self.__class_identifier):
                self.extensions.append(ctx.IDENTIFIER().getText())
        elif(ctx.IMPLEMENTS() is not None):
            if(ctx.IDENTIFIER().getText() not in self.extensions and self.__class_identifier in ctx.typeList().getText().split(',')):
                self.implementations.append(ctx.IDENTIFIER().getText())

class SymbolTable:
    def __init__(self):
        self.data = {}
        self.class_names = set()
    def AddnewClass(self, class_name):
        self.class_names.add(class_name)
    def IsClassName(self, name):
        return name in self.class_names
    def Insert(self, scope_list , identifier: str, type: str):

        key = '{}.{}'.format('.'.join(scope_list), identifier)
        if(key in self.data):
            print("Compile error. Cannot define variables with same names in same scope!")
            return False
        self.data[key] = type
    def FindVariableType(self, scope_list, identifier: str):
        result = None
        scope = scope_list[0]
        for idx, item in enumerate(scope_list):
            if(idx != 0):
                scope = "{}.{}".format(scope, item)
            key = '{}.{}'.format(scope, identifier)
            if(key in self.data):
                result = self.data[key]
        return result

class ScopeHandler:
    def __init__(self):
        self.__used_functions = {}
        self.__scope = ['MainFile_']
        self.__exited_blocks = []
        self.variable_declarating = False
    def enterVariableDeclaration(self):
        self.variable_declarating = True
    def exitVariableDeclaration(self):
        self.variable_declarating = False
    def enterClass(self, class_name):
        self.__scope.append(class_name)
    def exitClass(self, class_name):
        if (self.__scope[-1] != class_name):
            print("problem with your scopes!")
        else:
            self.__scope.remove(self.__scope[-1])
    def enterMethod(self, method_name):
        if(method_name in self.__used_functions):
            self.__used_functions[method_name] += 1
        else:
            self.__used_functions[method_name] = 0
        self.__scope.append("{}_{}".format(method_name, self.__used_functions[method_name]))
    def exitMethod(self, method_name):
        if (self.__scope[-1] != "{}_{}".format(method_name, self.__used_functions[method_name])):
            print("problem with your scopes!")
        else:
            self.__scope.remove(self.__scope[-1])
    def enterBlock(self):
        self.__scope.append("block_{}".format(len(self.__exited_blocks)))
        self.__exited_blocks.append(False)
    def exitBlock(self):
        # identify last not exited block
        block_number = None
        for idx, item in enumerate(self.__exited_blocks):
            if not item:
                block_number = idx
        if (block_number is None or self.__scope[-1] != "block_{}".format(block_number)):
            print("I have problems with blocks scope!")
            return
        self.__scope.remove(self.__scope[-1])
        self.__exited_blocks[block_number] = True
    def getScope(self):
        return self.__scope
