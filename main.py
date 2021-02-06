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
from refactorings.rcf import RemoveControlFlagRefactoringListener
from refactorings.rename_method import RenameMethodListener, ImplementaionIdentificationListener

extensions = []
implementations = []
#from speedy.src.java9speedy.parser import sa_java9_v2
def main(args):
    global extensions
    global implementations
    stream = FileStream(args.file, encoding='utf8')
    lexer = JavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParserLabeled(token_stream)
    tree = parser.compilationUnit()

    class_id = 'Piece'
    field_id = "y"
    new_field_id = "Y_CHANGED"
    if(args.method == 'rename_method'):
        my_listener = RenameMethodListener(
            common_token_stream=token_stream,
            class_identifier=class_id ,
            method_name="printG",
            new_method_name="newName",
            is_static=False,
            extentions=extensions,
            implementations=implementations)

    elif(args.method == 'rename_field'):
        my_listener = RenameFieldRefactoringListener(
            common_token_stream = token_stream,
            class_identifier = class_id,
            field_identifier = field_id,
            new_field_identifier = new_field_id,
            extentions = extensions,
            implementations = implementations)

    elif(args.method == 'remove_control_flag'):
        my_listener = RemoveControlFlagRefactoringListener(common_token_stream=token_stream)
    elif(args.method == "inheritance_relations"):
        my_listener = ImplementaionIdentificationListener(class_id)
    walker = ParseTreeWalker()
    walker.walk(t=tree, listener=my_listener)
    if(args.method == 'inheritance_relations'):
        extensions.extend(my_listener.extensions)
        implementations.extend(my_listener.implementations)
        return
    with open('input.refactored.java', mode='w', newline='') as f:
        f.write(my_listener.token_stream_rewriter.getDefaultText())


import os
import shutil


def recursive_walk(directory, method):
    for dirname, dirs, files in os.walk(directory):
        try:
            os.mkdir(dirname.replace("..", "refactored"))
        except:
            pass
        for filename in files:
            filename_without_extension, extension = os.path.splitext(filename)
            if(extension == '.java'):
                process_file("{}/{}".format(dirname, filename), method)
            shutil.copyfile("input.refactored.java", dirname.replace("..", "refactored") + "/" + filename)


        # for dir in dirs:
        #     recursive_walk("{}/{}".format(directory, dir), method)
def process_file(file, method):
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=file)
    argparser.add_argument(
        '--method', help='Refactoring Method', default=method)

    args = argparser.parse_args()
    main(args)

if __name__ == '__main__':
    try:
        os.mkdir("refactored")
    except:
        shutil.rmtree("refactored")
        os.mkdir("refactored")

    directory = '../Chess/'
    # recursive_walk(directory, 'inheritance_relations') # for test on a project
    # recursive_walk(directory, 'rename_field')
    process_file(r'rcf.java', 'remove_control_flag')
