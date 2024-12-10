from fpdf import FPDF

def create_invoice(customer_name, items):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Invoice')
    pdf.ln(10)
    pdf.set_font('Arial', size=12)
    pdf.cell(40, 10, f'Customer: {customer_name}')
    pdf.ln(10)
    total = 0
    for item, price in items.items():
        pdf.cell(40, 10, f'{item}: ${price}')
        pdf.ln(8)
        total += price
    pdf.ln(10)
    pdf.cell(40,10,f'Total: {total}')
    pdf.output('invoice.pdf')
    print('Invoice Generated')

create_invoice('John Cena', {'Laptop': 100, 'Headphones':10})