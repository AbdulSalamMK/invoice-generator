from fpdf import FPDF
import os
from datetime import datetime

class InvoicePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "INVOICE", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def generate_invoice(customer_name, items):
    pdf = InvoicePDF()
    pdf.add_page()

    # Add customer name and date
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Customer Name: {customer_name}", ln=True)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d')}", ln=True)
    pdf.ln(10)

    # Table headers
    pdf.set_font("Arial", "B", 12)
    pdf.cell(80, 10, "Item", 1)
    pdf.cell(30, 10, "Quantity", 1)
    pdf.cell(40, 10, "Price", 1)
    pdf.cell(40, 10, "Total", 1, ln=True)

    pdf.set_font("Arial", size=12)
    grand_total = 0
    for item in items:
        name, qty, price = item
        total = qty * price
        grand_total += total
        pdf.cell(80, 10, name, 1)
        pdf.cell(30, 10, str(qty), 1)
        pdf.cell(40, 10, f"{price:.2f}", 1)
        pdf.cell(40, 10, f"{total:.2f}", 1, ln=True)

    # Grand total
    pdf.set_font("Arial", "B", 12)
    pdf.cell(150, 10, "Grand Total", 1)
    pdf.cell(40, 10, f"{grand_total:.2f}", 1, ln=True)

    # Save file
    filename = f"invoice_{customer_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
    pdf.output(filename)
    print(f"Invoice saved as {filename}")

# Sample data for testing
customer = "John Doe"
items = [
    ("Product A", 2, 50.00),
    ("Product B", 1, 30.00),
    ("Product C", 3, 20.00)
]

generate_invoice(customer, items)
