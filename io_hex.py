# IO functions for the hex decoder
from os import remove
from argparse import ArgumentParser

def read_file(file_name, binary=False):
    '''
    Reads in the file to decode
    :param file_name: Name of the file
    :param binary: If True, reads in binary mode from the file
    :returns: Content of the file, if error: FileNotFoundError
    '''
    try:
        stream = open(file_name, "r")
        for l in stream:
            yield l.strip()
        if binary:
            stream = open(file_name, "rb")
            for l in stream:
                yield l.strip()
    except FileNotFoundError as fnfe:
        return fnfe

def del_file(file_name):
    '''
    Deletes a file if not empty
    :param file_name: Name of the file
    :returns: True if successful, else FileNotFoundError
    '''
    try:
        remove(file_name)
        return True
    except FileNotFoundError as fnfe:
        return fnfe

def writeV_file(file_name, content):
    '''
    Write to file if verbose parameter was set to True
    :param file_name: Name of the file
    :param content: Content to write to the file
    :returns: If Error: FileExistError
    '''
    try:
        out = open(file_name, "w")
        out.write(content)
        out.close()
    except FileExistsError as fee:
        return fee

def write_file(file_name, content, binary=False):
    '''
    Writing to a file
    :param file_name: Name of the file
    :param content: Content to write to the file
    :param binary: If set, writing in binary mode
    :returns: If Error --> FileExistsError
    '''
    try:
        out = open(file_name, "a")
        out.write(content)
        out.close()
        if binary:
            out = open(file_name, "a+b")
            out.write(bytes(content, "utf-8"))
            out.close()
    except FileExistsError as fee:
        return fee

def file_aol(file_name):
    '''
    Gets the amount of lines of the file
    :param file_name: Name of the file
    :returns: Integer (amount of lines)
    '''

    try:
        stream = open(file_name, "r")
        line_amount = int(len(stream.readlines()))
        return line_amount
    except FileNotFoundError as fnfe:
        return fnfe

def arg_parsing():
    '''
    Argument parser for the command line
    :returns: Arguments to parse, if Error --> Exception
    '''
    try:
        parser = ArgumentParser()
        parser.add_argument("-i", "--input", type=str, help="Input file with hex (.txt)")
        parser.add_argument("-o", "--output", type=str, help="Output file decoded (.txt)")
        parser.add_argument("-v", "--verbose", action="store_true", help="Verbosity")
        args = parser.parse_args()
        return args
    except Exception as eo:
        return eo