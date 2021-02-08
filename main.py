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
def main(args, recursive):
    global extensions
    global implementations
    try:
        stream = FileStream(args.file, encoding='utf-8-sig')
    except UnicodeDecodeError:
        print(f"Couldn't process {args.file}: Unicode Error")
        return
    print(f'processing {args.file}')
    lexer = JavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParserLabeled(token_stream)
    tree = parser.compilationUnit()

    class_id = args.class_id
    field_id = args.member_id
    new_field_id = args.new_name
    method_name = args.member_id
    new_method_name = args.new_name
    if(args.method == 'rename_method'):
        my_listener = RenameMethodListener(
            common_token_stream=token_stream,
            class_identifier=class_id ,
            method_name=method_name,
            new_method_name=new_method_name,
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
    if recursive:
        with open(args.file.replace("..", "refactored"), mode='w', newline='') as f:
            f.write(my_listener.token_stream_rewriter.getDefaultText())
    else:
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
                process_file("{}/{}".format(dirname, filename), method, True)
                # shutil.copyfile("input.refactored.java", dirname.replace("..", "refactored") + "/" + filename)


        # for dir in dirs:
        #     recursive_walk("{}/{}".format(directory, dir), method)
def process_file(file, method, recursive):
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=file)
    argparser.add_argument(
        '--method', help='Refactoring Method', default=method)
    class_id = 'King'
    member_id = "canMove"
    new_member_id = "Z"
    argparser.add_argument('--class_id', help="Target Class Identifier", default=class_id)
    argparser.add_argument('--member_id', help="Target Identifier", default=member_id)
    argparser.add_argument('--new_name', help="New Name For Target Identifier", default=new_member_id)

    args = argparser.parse_args()
    main(args, recursive)

if __name__ == '__main__':
    try:
        os.mkdir("refactored")
    except:
        shutil.rmtree("refactored")
        os.mkdir("refactored")
    directory = '../TestProjects/Chess'
    directories = directory.split('/')
    current_dir = "refactored"
    for dir in directories[1:-1]:
        current_dir = current_dir + f'/{dir}'
        os.mkdir(current_dir)

    # recursive_walk(directory, 'inheritance_relations') # for test on a project
    # recursive_walk(directory, 'rename_method')
    process_file(r'rcf.java', 'remove_control_flag', False)
