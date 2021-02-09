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
from antlr4.TokenStreamRewriter import TokenStreamRewriter
extensions = []
implementations = []
process_aborted = False
error_list = []
#from speedy.src.java9speedy.parser import sa_java9_v2
def main(args, recursive):
    global extensions
    global implementations
    global process_aborted
    global error_list
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
            is_static=args.static=="True",
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
    elif(args.method == 'rename_method' and my_listener.abort):
        my_listener.token_stream_rewriter = TokenStreamRewriter(token_stream)
        # print(f"Error on applying refactoring. A method with the same name ({my_listener.new_method_name}) exists in file {args.file}")
        process_aborted = True
        error_list.append(f"Error on applying refactoring. A method with the same name ({my_listener.new_method_name}) exists in {args.file}:{my_listener.class_identifier}")
    if recursive:
        with open(args.file.replace("..", "refactored"), mode='w', newline='') as f:
            f.write(my_listener.token_stream_rewriter.getDefaultText())
    else:
        with open('input.refactored.java', mode='w', newline='') as f:
            f.write(my_listener.token_stream_rewriter.getDefaultText())


import os
import shutil


def recursive_walk(directory, method):
    global process_aborted
    for dirname, dirs, files in os.walk(directory):
        if(process_aborted):
            break
        try:
            os.mkdir(dirname.replace("..", "refactored"))
        except:
            pass
        for filename in files:
            filename_without_extension, extension = os.path.splitext(filename)
            if(extension == '.java'):
                process_file("{}/{}".format(dirname, filename), method, True)
                # shutil.copyfile("input.refactored.java", dirname.replace("..", "refactored") + "/" + filename)
    if(not process_aborted):
        return
    shutil.rmtree("refactored")
    os.mkdir("refactored")
    directories = directory.split('/')
    current_dir = "refactored"
    for dir in directories[1:-1]:
        current_dir = current_dir + f'/{dir}'
        os.mkdir(current_dir)
    for dirname, dirs, files in os.walk(directory):
        try:
            os.mkdir(dirname.replace("..", "refactored"))
        except FileExistsError:
            pass
        for filename in files:
            address = "{}/{}".format(dirname, filename)
            new_address = address.replace("..", "refactored")
            shutil.copyfile(address, new_address)


        # for dir in dirs:
        #     recursive_walk("{}/{}".format(directory, dir), method)
def process_file(file, method, recursive):
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=file)
    argparser.add_argument(
        '--method', help='Refactoring Method', default=method)
    class_id = 'JSONObject'
    member_id = "wrongValueFormatException"
    new_member_id = "SimpleFunction"
    is_static = "True"
    argparser.add_argument('--class_id', help="Target Class Identifier", default=class_id)
    argparser.add_argument('--member_id', help="Target Identifier", default=member_id)
    argparser.add_argument('--new_name', help="New Name For Target Identifier", default=new_member_id)
    argparser.add_argument('--static', help="New Name For Target Identifier", default=is_static)

    args = argparser.parse_args()
    main(args, recursive)

if __name__ == '__main__':
    try:
        os.mkdir("refactored")
    except:
        shutil.rmtree("refactored")
        os.mkdir("refactored")
    directory = '../TestProjects/JSON-java'
    directories = directory.split('/')
    current_dir = "refactored"
    for dir in directories[1:-1]:
        current_dir = current_dir + f'/{dir}'
        os.mkdir(current_dir)

    #recursive_walk(directory, 'inheritance_relations') # for test on a project
    #recursive_walk(directory, 'rename_method')

    process_file(r'rcf.java', 'remove_control_flag', False)
    if(len(error_list) == 0):
        print("Succeffuly done!")
    else:
        print(f'{len(error_list)} errors occured.')
        print('\n'.join(error_list))

