from dataclasses import dataclass
import os

from fpdf import FPDF
import win32api
import PyPDF2

class CreatePdf():
    
    def print_pdf(file_path):
        win32api.ShellExecute(0, "print", file_path, None, ".", 0)
    
    def format_pdf():
        # Ruta al archivo PDF que deseas imprimir
        pdf_file = os.path.join(os.getcwd(),'ticket.pdf')

        # Abrir el archivo PDF en modo lectura
        with open(pdf_file, "rb") as file:
            # Crear un objeto PDFReader
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Crear un nuevo objeto PDFWriter
            pdf_writer = PyPDF2.PdfWriter()
            
            # Agregar todas las páginas excepto la primera al objeto PDFWriter
            for page_num in range(1, len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)
            
            # Guardar el PDF resultante en un archivo temporal
            temp_pdf_file = os.path.join(os.getcwd(),'ticket.pdf')
            with open(temp_pdf_file, "wb") as temp_file:
                pdf_writer.write(temp_file)
            
            # Imprimir el PDF resultante
            CreatePdf.print_pdf(temp_pdf_file)

    def create_pdf(receipt, sales_received, client):
        @dataclass
        class BasePdf():
            rec = receipt.id
            fecha = receipt.create
            nit = client.nit
            name = client.name
        
        class PDF(FPDF, BasePdf):
            def header(self): 
                self.set_auto_page_break(True, margin = 0.5)          
                # Select Courier bold 7
                self.set_font('Courier', '', 8)
                self.set_margins(5, 20, 5)
                self.image('image.jpg', x=12, y=2, w=55, h=18.5)
                # Framed title
                self.cell(w=0, h=3,txt='Direccion: Av. Tupac Katari y 18 chuita'.upper(),border=0, align='C',ln=True)
                self.cell(w=0, h=3,txt='Tel:777-777-77'.upper(),border=0, align='C',ln=True)
                self.cell(w=0, h=3,txt='R E C I B O'.upper(),border=0, align='C',ln=True)
                self.dashed_line(x1=5, y1=29, x2=75, y2=29, dash_length=0.8, space_length=0.5)
                self.cell(w=0, h=3,txt=f'No Recibo: {self.rec}'.upper(),border=0, align='C',ln=True)
                self.cell(w=35, h=3,txt=f'Fecha: {self.fecha.date().strftime("%d-%m-%Y")}'.upper(),border=0, align='C',ln=False)
                self.cell(w=35, h=3,txt=f'Hora: {self.fecha.time().strftime("%H:%M:%S")}'.upper(),border=0, align='C',ln=True)
                self.cell(w=35, h=3,txt='',border=0, align='C',ln=False)
                self.cell(w=35, h=3,txt=f'Nombre: {self.name}'.upper(),border=0, align='C',ln=True)
                self.dashed_line(x1=5, y1=38, x2=75, y2=38, dash_length=0.8, space_length=0.5)
                #tilte Table
                self.cell(w=30, h=3,txt='PRODUCTO',border=0, align='L',ln=False)
                self.cell(w=8, h=3,txt='CANT',border=0, align='C',ln=False)
                self.cell(w=13, h=3,txt='PRECIO',border=0, align='L',ln=False)
                self.cell(w=19, h=3,txt='TOTAL',border=0, align='R',ln=True)
                self.dashed_line(x1=5, y1=41, x2=75, y2=41, dash_length=0.8, space_length=0.5)
                # Line break
                self.ln(0)
                
            def add_products(self, product):
                self.cell(w=30, h=3,txt=product['name'].upper(),border=0, align='L',ln=False)
                self.cell(w=8, h=3,txt=f"{product['count']}",border=0, align='C',ln=False)
                self.cell(w=13, h=3,txt=f"{product['price']} Bs",border=0, align='L',ln=False)
                self.cell(w=19, h=3,txt=f"{product['total']} Bs",border=0, align='R',ln=True)
                
            def add_sale(self, title, data, border):    
                self.cell(w=30, h=3,txt='',border=0, align='L',ln=False)
                self.cell(w=8, h=3,txt='',border=0, align='C',ln=False)
                self.cell(w=13, h=3,txt=title.upper(),border=border, align='L',ln=False)
                self.cell(w=19, h=3,txt=f'{(data)} Bs',border=border, align='R',ln=True)
            
        orientacion = 'P'
        medida = 'mm'
        tamaño = (80,150)
        
        pdf = PDF(orientacion, medida, tamaño)
        
        pdf.add_page()
        pdf.add_page()
        for order in sales_received:
            pdf.add_products(order)
        
        
            
        pdf.add_sale('TOTAL', receipt.sale_total, 'B')
        pdf.add_sale('RECIBIDO', receipt.received, '')
        pdf.add_sale('CAMBIO', receipt.change, '')
        
        pdf.cell(w=0, h=3,txt='',border=0, align='L',ln=True)
        pdf.cell(w=0, h=3,txt='GRACIAS POR SU COMPRA!!!',border=0, align='C',ln=True)
        
        pdf.output('ticket.pdf')
        CreatePdf.format_pdf()