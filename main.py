import pandas
from fpdf import FPDF
import glob
import glob
from pathlib import Path


filepaths=glob.glob('files/*.txt')
pdf = FPDF(orientation='L', format='a4', unit='mm')
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths:

    file_names=Path(filepath).stem.title()

    pdf.add_page()

    pdf.set_font(family='Times',size=20,style='B')
    pdf.cell(w=100,h=12,txt=f'{file_names}',ln=1)
    with open(filepath,'r') as file:
        content= file.read()

        pdf.set_font(family='Times',size=10,style='I')

        pdf.multi_cell(w=0, h=6, txt=f'{content}')

pdf.output('output.pdf')



