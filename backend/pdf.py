from weasyprint import HTML

def create_pdf(images):
    html = "<html><body>"
    for img in images:
        html += f'<img src="{img}" style="width:100%"/>'
    html += "</body></html>"

    HTML(string=html).write_pdf("output.pdf")

    return "output.pdf"
