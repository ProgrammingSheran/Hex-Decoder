import re
from codecs import decode
from os import remove

class HexDecoder:

    def __init__(self, in_file, out_file, verbose=False):
        self.in_file = in_file
        self.out_file = out_file
        self.verbose = verbose
        self.decode()

    def readFile(self):
        try:
            stdin_stream = open(self.in_file, "r", encoding="utf-8")
            return stdin_stream
        except FileNotFoundError:
            print("File not Found!")

    def del_if_not_empty(self, file_name):
        try:
            remove(file_name)
        except FileNotFoundError:
            print("File doesn't exist!")

    def writeFile(self, content, binary=False):
        try:
            out_file = open(self.out_file, "a+", encoding="utf-8")
            if not binary:
                out_file.write(str(content))
            else:
                out_file = open(self.out_file, "ab", encoding="utf-8")
                out_file.write(bytes(content))
        except FileExistsError:
            print("File you want to write to already exists!")

    def decode(self):
        self.del_if_not_empty(self.out_file)

        for line in self.readFile():
            l = line.strip()
            l_match = re.match(r"\d+:", l)
            line_number = l_match.string[0:l_match.span()[1]].replace(":", "")
            c_match = re.findall(r"\d\w", l)
            c_match.pop(0)
            elements = "".join(c_match)
            decoded = decode(elements, "hex").decode()
            result = line_number + ": " + decoded + "\n"
            self.writeFile(result)

h = HexDecoder("Input-File.txt", "Output-File.txt")