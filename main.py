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
from gen.javaLabeled.JavaLexer import JavaLexer
from gen.javaLabeled.JavaParserLabeled import JavaParserLabeled
from refactorings.rename_method import RenameMethodListener
from refactorings.rcf import RemoveControlFlagRefactoringListener

#from speedy.src.java9speedy.parser import sa_java9_v2

def main(args):
    # Step 1: Load input source into stream
    stream = FileStream(args.file, encoding='utf8')
    # input_stream = StdinStream()

    # Step 2: Create an instance of AssignmentStLexer
    lexer = JavaLexer(stream)
    # Step 3: Convert the input source into a list of tokens
    token_stream = CommonTokenStream(lexer)
    # Step 4: Create an instance of the AssignmentStParser
    parser = JavaParserLabeled(token_stream)
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
    if(args.method == 'rename_method'):
        my_listener = RenameMethodListener(common_token_stream=token_stream, class_identifier='A' ,method_name="printG", new_method_name="printg")
    elif(args.method == 'rename_field'):
        my_listener = RenameFieldRefactoringListener(common_token_stream=token_stream, class_identifier="SequenceDiagramModule", field_identifier="propPanelFactory", new_field_identifier="PPT")
    elif(args.method == 'remove_control_flag'):
        my_listener = RemoveControlFlagRefactoringListener(common_token_stream=token_stream)
        #my_listener = RenameFieldRefactoringListener(common_token_stream=token_stream, class_identifier="C", field_identifier="g", new_field_identifier="gg")

    # return
    walker = ParseTreeWalker()
    walker.walk(t=tree, listener=my_listener)

    with open('input.refactored.java', mode='w', newline='') as f:
        f.write(my_listener.token_stream_rewriter.getDefaultText())


import os


def recursive_walk(directory):
    for dirname, dirs, files in os.walk(directory):
        for filename in files:
            filename_without_extension, extension = os.path.splitext(filename)
            if(extension == '.java'):
                process_file("{}/{}".format(directory, filename))
        for dir in dirs:
            recursive_walk("{}/{}".format(directory, dir))
def process_file(file):
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=file)
    argparser.add_argument(
        '--method', help='Refactoring Method', default='remove_control_flag')

    args = argparser.parse_args()
    main(args)

if __name__ == '__main__':
    directory = '../xerces2-j/src'
    # recursive_walk(directory) # for test on a project
    process_file(r'input2.java')
