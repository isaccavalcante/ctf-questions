#import pdfkit 
import weasyprint


def parse_template(name, cpf):
    if not name:
        name = ""
    if not cpf:
        cpf = ""
    html_filename = f'invoice-{name}-{cpf}.html' 
    with open("templates/invoice.html", encoding="utf-8") as f:
        parsed_template = f.read().replace("{{ name }}", name).replace("{{ cpf }}", cpf)
    with open(html_filename, "w") as f:
        f.write(parsed_template)
    return html_filename


def generate_invoice(name, cpf):
    html_filename = parse_template(name, cpf)
    pdf_filename = html_filename.replace(".html", ".pdf")    
    html = weasyprint.HTML(html_filename)
    html.write_pdf(pdf_filename)
    return pdf_filename
