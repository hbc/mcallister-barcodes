"""
this script it to pull out barcodes for Jessica's experiment
from the McAllister lab
"""
from argparse import ArgumentParser
import regex as re

def stream_fastq(file_handler):
    """"
    Generator which gives all four lines if a fastq read as one string
    (snagged from https://github.com/vals/umis)
    """
    next_element = ''
    for i, line in enumerate(file_handler):
        if i % 4 == 1:
            yield line

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("fastq")
    args = parser.parse_args()

    parser_re = re.compile("(?P<index>\w{8})(\w{17})(ACGCGT)(?P<barcode>\w{24})(CTGCAG)")
    print "barcode", "index"
    fq_handle = stream_fastq(open(args.fastq))
    for read in fq_handle:
        match = parser_re.match(read)
        if match:
            barcode = match.group('barcode')
            index = match.group('index')
            print barcode, index
