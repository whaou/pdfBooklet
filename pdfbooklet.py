#!/usr/bin/env python3

from pypdf import PdfWriter, PdfReader
from argparse import ArgumentParser

def bookletOrder(nbPages):
    # Round number of pages to the upper multiple of 4
    n = nbPages
    if n%4 != 0:
        n += 4 - n%4
    
    # Build the list
    l = []
    end = n
    for i in range(0, int(n/2), 2):
        l.append(i+1)
        l.append(i+2)
        l.append(end-i-1)
        l.append(end-i)
    return l


def reorderPdfInBookletOrder(inputFilePath, outputFilePath):
    output_pdf = PdfWriter()

    with open(inputFilePath, 'rb') as inFile:
        input_pdf = PdfReader(inFile)
        inPages = len(input_pdf.pages)

        for page in bookletOrder(inPages):
            if page <= inPages:
                output_pdf.add_page(input_pdf.pages[page-1])
            else:
                output_pdf.add_blank_page()

        with open(outputFilePath, "wb") as writefile:
            output_pdf.write(writefile)


if __name__ == "__main__":
    parser = ArgumentParser(
            description = 'Reorder a PDF to print it in a booklet order')
    parser.add_argument('inputFile',
                        type=str,
                        help='Path of the file to convert')
    parser.add_argument('outputFile',
                        type=str,
                        help='Path of the file to write')
    args = parser.parse_args()
    
    reorderPdfInBookletOrder(args.inputFile, args.outputFile)


