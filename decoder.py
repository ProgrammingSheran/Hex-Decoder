import re
from codecs import decode
from io_hex import del_file, read_file, write_file, writeV_file
from datetime import datetime

class HexDecoder:

    '''
    >>> h = HexDecoder("blubb.txt", "Bl.txt", verbose=True)
    >>> [result for result in h.decoding()]
    [(1, 'Hey how are you?'), (2, 'This is a test!'), (3, 'My Hex-Decoder = True')]
    '''

    VERSION = "v0.2"

    def __init__(self, in_file, out_file, verbose=False):
        self.in_file = in_file
        self.out_file = out_file
        self.verbose = verbose

    def verbose_info(self):
        '''Puts info at the beginning of the file, if verbose parameter was set to True'''

        if self.verbose:
            info = "Decoded with Hex-Decoder %s\n" % self.VERSION
            time = "Date: " + datetime.now().strftime("%d.%m.%y - %H:%M:%S") + "\n\n"
            to_file = info + time
            writeV_file(self.out_file, to_file)
        else:
            pass

    def decoding(self):
        '''
        Main decoding function
        :returns: Decoded hex from input as an iterable object
        '''

        df = del_file(self.out_file)
        if not df:
            print(df)
        try:
            self.verbose_info()
            for line in read_file(self.in_file):
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


if __name__ == '__main__':
    import doctest
    doctest.testmod()