from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def pdf_export_agent(report: str, filename: str = "report.pdf"):

    file = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    lines = report.split("\n")

    y = height - 50

    for line in lines:

        if y < 50:
            file.showPage()
            y = height - 50

        if line.startswith("#"):
            file.setFont("Helvetica-Bold", 12)
        else:
            file.setFont("Helvetica", 10)

        file.drawString(40, y, line[:100])
        y -= 15

    file.save()

    return filename