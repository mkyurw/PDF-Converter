import PyPDF2
import sys

# Run the python file in the same folder as the pdf file
# The order of merging depends on the order of your input files
inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('Merged.pdf')

pdf_merger(inputs)