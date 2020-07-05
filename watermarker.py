import PyPDF2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--watermark", "-w", required=True, help="input watermark.pdf")
parser.add_argument("--input", "-i", required=True, help="input the file you want to be watermarked")

args = vars(parser.parse_args())

watermark = args['watermark']
input_file = args['input']

with open(f'{input_file}', 'rb'):
    input_reader = PyPDF2.PdfFileReader(input_file)

with open (f'{watermark}', 'rb'):
    watermark_reader = PyPDF2.PdfFileReader(watermark)

output_writer = PyPDF2.PdfFileWriter()

for i in range(input_reader.getNumPages()):
    page = input_reader.getPage(i)
    page.mergePage(watermark_reader.getPage(0))
    output_writer.addPage(page)

    with open('output.pdf', 'wb') as output:
        output_writer.write(output)
print('Your Document is watermarked')