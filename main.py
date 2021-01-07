"""

The main module of CodART

-changelog
-- Add C++ backend support

"""

__version__ = '0.2.0'
__author__ = 'Morteza'


import argparse

from antlr4 import *

#from refactorings.extract_class import ExtractClassRefactoringListener
from refactorings.rename_field import RenameFieldRefactoringListener
from gen.java9.Java9_v2Lexer import Java9_v2Lexer
from gen.java9.Java9_v2Parser import Java9_v2Parser

#from speedy.src.java9speedy.parser import sa_java9_v2

def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    # input_stream = StdinStream()

    # Step 2: Create an instance of AssignmentStLexer
    lexer = Java9_v2Lexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)
    # Step 4: Create an instance of the AssignmentStParser
    parser = Java9_v2Parser(token_stream)
    #parser.getTokenStream()

    # Step 5: Create parse tree
    # 1. Python backend --> Low speed
    # parse_tree = parser.compilationUnit()

    # 2. C++ backend --> high speed

    #parse_tree = sa_java9_v2.parse(stream, 'compilationUnit', None)
    #quit()
    # Step 6: Create an instance of AssignmentStListener
    #my_listener = ExtractClassRefactoringListener(common_token_stream=token_stream, class_identifier='Worker')
    tree = parser.compilationUnit()
    my_listener = RenameFieldRefactoringListener(common_token_stream=token_stream, class_identifier="A", field_identifier="g", new_field_identifier="gg")

    # return
    walker = ParseTreeWalker()
    walker.walk(t=tree, listener=my_listener)

    with open('input.refactored.java', mode='w', newline='') as f:
        f.write(my_listener.token_stream_rewriter.getDefaultText())


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.java')
    args = argparser.parse_args()
    main(args)
