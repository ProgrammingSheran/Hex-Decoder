import re
from codecs import decode
from io_hex import read_file, del_file, write_file

class HexDecoder:

    '''
    >>> h = HexDecoder("blubb.txt", "Bl.txt")
    >>> [result for result in h.decoding()]
    [(1, 'Hey how are you?'), (2, 'This is a test!'), (3, 'My Hex-Decoder = True')]
    '''

    def __init__(self, in_file, out_file, verbose=False):
        self.in_file = in_file
        self.out_file = out_file
        self.verbose = verbose

    def decoding(self):
        '''
        Main decoding function
        :returns: Decoded hex from input as an iterable object
        '''

        df = del_file(self.out_file)
        if not df:
            print(df)
        try:
            r_file = read_file(self.in_file)
            for line in f_file:
                l = line.strip()
                l_match = re.match(r"\d+:", l)
                line_number = l_match.string[0:l_match.span()[1]].replace(":", "")
                c_match = re.findall(r"\d\w", l)
                c_match.pop(0)
                elements = "".join(c_match)
                decoded = decode(elements, "hex").decode()
                file_result = line_number + ": " + decoded + "\n"
                result = (line_number, decoded)
                if line_number.isdigit():
                    result = (int(line_number), decoded)
                write_file(self.out_file, file_result)
                yield result
        except Exception as e:
            return e

if __name__ == "__main__":
    import doctest
    doctest.testmod()
